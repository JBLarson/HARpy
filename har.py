#!/usr/bin/python3

import json
import sys

def analyze_har(file_path):
        with open(file_path, 'r') as f:
                har_data = json.load(f)

        total_size = 0
        total_requests = 0
        content_types = {}

        for entry in har_data['log']['entries']:
                total_requests += 1
                size = entry['response']['content']['size']
                total_size += size
                content_type = entry['response']['content']['mimeType']

                if content_type not in content_types:
                        content_types[content_type] = {'count': 0, 'size': 0}

                content_types[content_type]['count'] += 1
                content_types[content_type]['size'] += size

        print(f'Total requests: {total_requests}')
        print(f'Total size: {human_readable_size(total_size)}')
        print('Content types:')
        for content_type, data in content_types.items():
                print(f'  {content_type}: {data["count"]} requests, {human_readable_size(data["size"])}')

def human_readable_size(size):
        if size < 10_000:
                return f"{size} bytes"

        for unit in ['KB', 'MB', 'GB', 'TB']:
                size /= 1024
                if size < 1024:
                        break
        return f"{size:.1f} {unit}"

if __name__ == '__main__':
        if len(sys.argv) < 2:
                print('Usage: python har_analyzer.py path_to_har_file')
                sys.exit(1)

        file_path = sys.argv[1]
        analyze_har(file_path)
