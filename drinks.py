#!/usr/bin/env python2

from __future__ import print_function
#import ldap
import sys

seen_already = []

try:
    with open('seen.txt', 'r') as seen_file:
        seen_already = seen_file.readlines()
        seen_already = [x.strip() for x in seen_already]
except IOError:
    pass

ecs_ids = []

try:
    with open('ids.txt', 'r') as ids_file:
        ecs_ids = ids_file.readlines()
        ecs_ids = [x.strip() for x in ecs_ids]
except IOError:
    pass


#l = ldap.initialize('ldap://ldap.soton.ac.uk')

#binddn = "mwrc1g12@soton.ac.uk"
#basedn = "dc=soton,dc=ac,dc=uk"
#search_filter = "(division=ECS)"
#search_attr = ["employeeID"]
#search_scope = ldap.SCOPE_SUBTREE

#l.simple_bind_s(binddn)

#print(l.search_s(basedn, search_scope, search_filter, search_attr))
#sys.exit(0)

with open('seen.txt', 'a') as seen_file:
    while True:
        id_number = raw_input()
        if id_number in seen_already:
            print("""
888b    888          888 
8888b   888          888 
88888b  888          888 
888Y88b 888  .d88b.  888 
888 Y88b888 d88""88b 888 
888  Y88888 888  888 Y8P 
888   Y8888 Y88..88P  "  
888    Y888  "Y88P"  888
""")
            continue
        if not id_number in ecs_ids:
            print("""
888b    888          888 
8888b   888          888 
88888b  888          888 
888Y88b 888  .d88b.  888 
888 Y88b888 d88""88b 888 
888  Y88888 888  888 Y8P 
888   Y8888 Y88..88P  "  
888    Y888  "Y88P"  888
""")
            print("FILTHY NON-ECS GATECRASHER")
        else:
            print("""
Y88b   d88P                888 
 Y88b d88P                 888 
  Y88o88P                  888 
   Y888P  .d88b.  .d8888b  888 
    888  d8P  Y8b 88K      888 
    888  88888888 "Y8888b. Y8P 
    888  Y8b.          X88  "  
    888   "Y8888   88888P' 888
""")
            print(id_number, file=seen_file)
            seen_file.flush()
            seen_already.append(id_number)
