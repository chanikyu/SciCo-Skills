"""Send one request to an explicitly selected local VectorCraft instance."""
import argparse
import json
import socket
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, required=True)
    parser.add_argument('--timeout', type=float, default=55)
    parser.add_argument('method')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--params', default=None)
    group.add_argument('--params-file', type=Path)
    args = parser.parse_args()
    try:
        raw = args.params_file.read_text() if args.params_file else args.params or '{}'
        params = json.loads(raw)
        if not isinstance(params, dict):
            raise ValueError('params must be a JSON object')
        request = {'id': 1, 'method': args.method, 'params': params}
        with socket.create_connection(('127.0.0.1', args.port), args.timeout) as sock:
            sock.settimeout(args.timeout)
            with sock.makefile('rwb') as stream:
                stream.write((json.dumps(request) + '\n').encode())
                stream.flush()
                reply = json.loads(stream.readline())
        print(json.dumps(reply, ensure_ascii=False))
        return 0 if reply.get('ok') else 1
    except (OSError, ValueError) as exc:
        print(f'Control request failed: {exc}. Inspect app/document state before retrying mutations.', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
