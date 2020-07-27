import pandas as pd

# initialize list of lists
data = [['tom', "time", "Status"]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Time', "Status"])


to_append = ['pd new', "time", 'liked']
df_length = len(df)
df.loc[df_length] = to_append

# row 0, column 1
print(df.iloc[0][2])

# print dataframe.
print(df)

exit()

 #get first 10 posts names
while column_index <= 10:

    try:
        # Insert your scraping action here
        # Use xpath for posts but increment article number by 1
        xpath_table = '//*[@id="react-root"]/section/main/section/div/div[3]/div/article[' + str(column_index) + ']/header/div[2]/div[1]/div/span/a'
        celltext = driver.find_element_by_xpath(xpath_table)
        top_cell = celltext.text
        list_of_profiles[column_index - 1] = top_cell
        column_index += 1
        print(column_index)

    except NoSuchElementException:
        # Just append a None or ""
        print("error handling enagged!!")
        print("looking for", column_index)
        scroll_wheel("down", 20)





print("posts", list_of_profiles)
