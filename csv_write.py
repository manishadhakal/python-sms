from csv import writer,DictWriter
# with open('employee1.csv','w') as f:
#     csv_reader=writer(f)
#     csv_reader.writerow(['name','contact'])
#     csv_reader.writerow(['sagar','9821559200'])
#     csv_reader.writerow(['salin','982156778'])
with open('employee12.csv','w') as f:
    fieldnames=['firstname','lastname']
    csv_reader=DictWriter(f,fieldnames=fieldnames)
    csv_reader.writeheader()
    csv_reader.writerow({'firstname':'sagar','lastname':'malla'})

    # csv_reader.writerow(['sagar','9821559200'])
    # csv_reader.writerow(['salin','982156778'])

    # csv_reader.writerows([['name','phone'],['samir','98374893'],['manish','983773738']])


