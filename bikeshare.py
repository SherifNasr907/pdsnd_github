import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid
    # inputs
    city_name = ''
    while city_name not in CITY_DATA:
        city_name = input("Please enter the name of the city you want to analyze,\nEnter either chicago, washington, "
                          "new york city\n: ").lower()
        if city_name.lower() in CITY_DATA:
            city = CITY_DATA[city_name.lower()]
        else:
            print("Invalid input!\nKindly enter chicago, washington, or new york city!")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name not in MONTH_DATA:
        month_name = input("Please indicate the month filter\nEnter either january, february, march, april, may, "
                           "june\nOr use all to skip month filter: ").lower()
        if month_name.lower() in MONTH_DATA:
            month = month_name.lower()
        else:
            print("Sorry, couldn't get your input, Kindly enter the month title or use all to show all months data "
                  "analysis!")
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name not in DAY_DATA:
        day_name = input("Kindly enter the day filter\nEnter either sunday, monday, tuesday, wednesday, thursday, "
                         "friday, or saturday\nOr use all to show data analysis for all the week days\n Enter week "
                         "day: ").lower()
        if day_name.lower() in DAY_DATA:
            day = day_name.lower()
        else:
            print(
                "Invalid input!\nKindly Enter any week day to filter the data with, or use all to show all week data!")
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Week Day'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = MONTH_DATA.index(month)
        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Week Day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    print("The most common month from the given filtered data is: ", str(common_month).title())
    # TO DO: display the most common day of week
    common_day = df['Week Day'].mode()[0]
    print("The most common week day for the given filtered data is: ", str(common_day).title())
    # TO DO: display the most common start hour
    common_hour = df['Hour'].mode()[0]
    print("The most popular hour to start a trip is: ", str(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common Start Station is: ", str(common_start_station))
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common End Station is: ", str(common_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is: ", frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    def convert(seconds):
        """Shows the time stat in a more readable way."""
        min, sec = divmod(seconds, 60)
        hour, min = divmod(min, 60)
        return "%d:%02d:%02d" % (hour, min, sec)

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is: \nHH:MIN:SEC\n", convert(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The average travel time is: \nHH:MIN:SEC\n", convert(mean_travel_time))
    # display the longest trip
    longest_trip = df['Trip Duration'].max()
    print("The longest trip took: \nHH:MIN:SEC\n", convert(longest_trip))
    # display the shortest trip
    shortest_trip = df['Trip Duration'].min()
    print("The shortest trip took: \nHH:MIN:SEC\n", convert(shortest_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User counts as the following:\n", str(user_types))
    # TO DO: Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
        print("The count of users gender is: ", str(gender))
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print("The earliest birth year is: ", earliest_year)
        recent_birth_year = df['Birth Year'].max()
        print("The most recent birth year is: ", recent_birth_year)
        common_year = df['Birth Year'].mode()[0]
        print("The most common year of birth is: ", common_year)
    else:
        print("No Gender data nor Birth year data available for Washington")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def raw_data(df):
    """Ask the user if s/he wants to show the raw data"""
    user_input = input('\nDo you want to see raw data? Enter no or press any key to show 5 rows of data.\n')
    line_number = 0

    while True:
        if user_input.lower() != 'no':
            print(df.iloc[line_number: line_number + 5])
            line_number += 5
            user_input = input('\nDo you want to see more raw data? Enter no \nOr any other key to show more raw '
                               'data.\n')
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter y \nOr any other key to quit\n').lower()
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
    main()
