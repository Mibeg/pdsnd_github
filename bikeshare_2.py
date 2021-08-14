import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

ddef get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ("chicago","new york city","washington")
    city = input("Enter the city you need the data for: Chicago, New York City or Washington? ").lower()
    while city not in cities:
        print("Please, select one of the following cities:")
        city = input("Chicago, New York City or Washington")
    print ("The city you selected is: " + city)
    # get user input for month (all, january, february, ... , june)
        months = ("all","january","february","march","april","may","june")
    month = input("Enter the month you are interested in: All, January, February, March, April, May or June? ").lower()
    while month not in months:
        print("Please, select one of the following months:")
        month = input("All, January, February, March, April, May or June")
    print ("The month you selected is " + month)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ("all","monday","tuesday","wednesday","thrusday","friday","saturday","sunday")
    day = input("Enter the day you are interested in: All, Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday or Sunday? ").lower()
    while day not in days:
        print("Please, select one of the following days: ")
        day = input("All, Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday or Sunday")
    print ("The day you selected is " + day)
        print('-'*40)
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        # use the index of the days list to get the corresponding int
        days = ['monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        # filter by day of week to create the new dataframe
        #df = df[df['day_of_week'] == day.title()]
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    print("The month when travels are most frecuent is ", df['month'].value_counts().idxmax())
    # display the most common day of week
    print("The day of the week when travels are most frecuent is ", df['day_of_week'].value_counts().idxmax())
    # display the most common start hour
    print("The most frecuent travel start hour is ", df['Start Time'].dt.hour.value_counts().idxmax())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    print("The most commonly used start station is", df['Start Station'].value_counts().idxmax())
    #print(df['Start Station'].mode())
    # display most commonly used end station
    print("The most commonly used end station is", df['End Station'].value_counts().idxmax())
    # display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip is", df.groupby(['Start Station','End Station']).size().idxmax())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    print("The total travel time is ", df['Trip Duration'].sum())
       # display mean travel time
    print("The average travel time is ", df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    print("The user types are ", df.groupby("User Type").size() )
        # Display counts of gender - Washington NO
    if 'Gender' in df.columns:
        print("The gender is ", df.groupby("Gender").size() )
    # Display earliest, most recent, and most common year of birth - Washington NO
    if 'Birth Year' in df.columns:
        print("The earliest year of birth is ", df["Birth Year"].min() )
        print("The most recent year of birth is ", df["Birth Year"].max() )
        print("The most common year of birth is ", df["Birth Year"].mode() )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    view_data = input("Would you like to view the first 5 rows of individual trip data? Enter yes or no?").lower()
        start_loc = 0
    while (view_data=="yes"):
        print(df.iloc[start_loc:start_loc+5,:])
        start_loc += 5
        view_data = input("Do you want to see the next 5 rows of data?: yes or no ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
