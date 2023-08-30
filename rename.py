import os

# Function to rename tables
def main():
	i = 2528
	path="C:/Users/FOKO BRICE/Desktop/SecuTable/test/tables/file/"
	for filename in os.listdir(path):
		my_dest ="table" + str(i) + ".csv"
		my_source =path + filename
		my_dest =path + my_dest
		# rename() function will
		# rename all the files
		os.rename(my_source, my_dest)
		i += 1
# Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()