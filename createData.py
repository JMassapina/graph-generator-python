import names
import csv
from random import randint

def generate_users(num_users, users_file_path):
    with open(users_file_path, 'wb') as csv_file:
        wr = csv.writer(csv_file)
        # Add header to CSV.
        wr.writerow(('user_id', 'name'))
        i = 1
        while i in range (1, num_users + 1):
            user_item = []
            user_item.append(i)
            # Grab user name from 1990 Census data. Cool!
            user_item.append(names.get_full_name());
            wr.writerow(user_item)
            i = i + 1

def generate_pages(num_pages, pages_file_path):
    with open(pages_file_path, 'wb') as csv_file:
        wr = csv.writer(csv_file)
        wr.writerow(("page_id"))
        i = 1
        while i in range (1, num_users):
            page_item = []
            page_item.append(i)
            wr.writerow(page_item)
            i = i + 1

def generate_connections(num_users, num_pages, max_edges, edges_file_path):
    with open(edges_file_path, 'wb') as csv_file:
        wr = csv.writer(csv_file)
        wr.writerow(("user_id", "page_id"))
        i = 1
        while i in range (1, num_users + 1):
            # print "i: %i" % i
            i = i + 1
            rand = randint(0, max_edges)
            # print "rand: %r" % rand

            j = 0
            while j in range (0, rand):
                j = j + 1
                # print "j: %s" % j
                page_id = randint(1, num_pages)
                connection = []
                connection.append(i)
                connection.append(page_id)
                wr.writerow(connection)




num_users = 1000
num_pages = 100000
max_edges = 20

generate_users(num_users, '/home/sheldon/python_users.csv')
generate_pages(num_pages, '/home/sheldon/python_pages.csv')
generate_connections(num_users, num_pages, max_edges, '/home/sheldon/python_connections.csv')
