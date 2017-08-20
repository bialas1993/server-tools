import argparse, os, time, datetime

parser = argparse.ArgumentParser(description='Clean builds from gitlab CI.')
parser.add_argument('--path', metavar='p', help='is a directory with builds')
parser.add_argument('--expiration-days', metavar='e', type=int, help='to remove')

args = parser.parse_args()
path = os.path.abspath(args.path)
expiration_days = args.expiration_days
expiration_limit = datetime.datetime.now() - datetime.timedelta(days=expiration_days)

for dirname in os.listdir(path):
    if os.path.isdir(os.path.join(path, dirname)):
        file_create_time = datetime.datetime.strptime(
            time.ctime(os.stat(os.path.join(path, dirname)).st_ctime),
            "%a %b %d %H:%M:%S %Y"
        )
        if (expiration_limit - file_create_time).total_seconds() > 0:
            print "Removing %s" % dirname
            os.remove(os.path.join(path, dirname))

