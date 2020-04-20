import argparse


class StoreLower(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, str(values).lower())


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('x', action=StoreLower)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    print(args.x)
