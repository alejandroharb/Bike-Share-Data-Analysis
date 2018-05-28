import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nPlease enter a city (Chicago, New York City, Washington) \n')
        if city.lower() == 'chicago' or city.lower() == 'new york city' or city.lower() == 'washington':
            break


    # get user input for month (all, january, february, ... , june)
    while True:
        month_options = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = input('\nPlease enter a month (january, february, etc.) or enter "all" \n')
        if month.lower() in month_options:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_options = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input('\nPlease enter a day of the week (monday, tuesday, etc.) or enter "all" \n')
        if day.lower() in day_options:
            break

    print('-'*40)
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
    CITY_DATA = {
        'chicago': 'chicago.csv',
        'new york city':'new_york_city.csv',
        'washington':'washington.csv'
        }

    df = pd.read_csv(CITY_DATA[city])
    df['Gender'].fillna('Unknown', inplace = True)
    df['User Type'].fillna('Unknown', inplace = True)
    df['Birth Year'].fillna('Unknown', inplace = True)
    print(df.isnull().any())

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('\nMost common month is: {}.\n'.format(common_month))

    # display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    common_day = df['day'].mode()[0]
    print('\nMost common day is: {}.\n'.format(common_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('\nMost common start hour is: {}.\n'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\nMost commonly used START station is {}.\n'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('\nMost commonly used END station is {}.\n'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('\nThe most frequent combination of START STATION and END STATION: \n', df[['Start Station', 'End Station']].mode().loc[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\nTotal travel time is: {}.'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('\nThe travel time MEAN is: {}.'.format(df['Trip Duration'].mean()))

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nCounts of user types: \n', df['User Type'].value_counts())

    # Display counts of gender
    print('\nCounts of genders: \n', df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    print('\nMost common year of birth: {}'.format(df['Birth Year'].mode()[0]))
    print('\nMost recent year of birth: {}'.format(df['Birth Year'][[-1]]))
    print('\nEarliest year of birth data entry: {}'.format(df['Birth Year'][[0]]))

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
