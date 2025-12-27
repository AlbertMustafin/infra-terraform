import os
import argparse
from terraform import Terraform

def parse_args():
    parser = argparse.ArgumentParser(description='Infra Terraform')
    parser.add_argument('--action', type=str, required=True, help='Action to perform (apply, destroy, init)')
    parser.add_argument('--path', type=str, default='./', help='Path to terraform configuration')
    return parser.parse_args()

def main():
    args = parse_args()
    terraform = Terraform(working_dir=args.path)
    if args.action == 'apply':
        terraform.apply()
    elif args.action == 'destroy':
        terraform.destroy()
    elif args.action == 'init':
        terraform.init()
    else:
        raise ValueError('Invalid action')

if __name__ == '__main__':
    main()