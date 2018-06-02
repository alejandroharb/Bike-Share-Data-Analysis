import time
import pandas as pd
import numpy as np

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

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
        month = input('\nPlease enter a month (january - june) or enter "all" \n')
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

    #create month and day columns for filtering
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int

        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    #replace NaN values in dataset
    if city == 'chicago' or city == 'new_york_city':
        df['Gender'].fillna('Unknown', inplace = True)
        df['Birth Year'].fillna(df['Birth Year'].mode()[0], inplace = True)

    df['User Type'].fillna('Unknown', inplace = True)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    #print section
    print_title("Popular Times of Travel")

    start_time = time.time()

    common_month_index = df['month'].mode()[0]
    #bringing back to zero-index
    common_month = MONTHS[common_month_index - 1]
    print('\nMost common month is: {}.\n'.format(common_month))

    # display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    common_day = df['day'].mode()[0]
    print('\nMost common day is: {}.\n'.format(common_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('\nMost common start hour is: {}.\n'.format(common_hour))

    print_times(start_time)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    #print section
    print_title("Popular Station and Trip")

    start_time = time.time()

    # display most commonly used start station
    print('\nMost commonly used START station is {}.\n'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('\nMost commonly used END station is {}.\n'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('\nThe most frequent combination of START STATION and END STATION: \n', df[['Start Station', 'End Station']].mode().loc[0])

    print_times(start_time)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    #print section
    print_title("Trip Duration")

    start_time = time.time()

    # display total travel time
    print('\nTotal travel time is: {}.'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('\nThe travel time MEAN is: {}.'.format(df['Trip Duration'].mean()))

    print_times(start_time)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    #print section
    print_title("User Info")

    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nCounts of user types: \n', user_types)

    # Display counts of gender
    if city == 'chicago' or city == 'new_york_city':
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of genders: \n', gender_counts)
        # Display earliest, most recent, and most common year of birth
        common_birth_year = int(df['Birth Year'].mode()[0])
        recent_birth_year = int(df['Birth Year'].iloc[-1])
        earliest_birth_year = int(df['Birth Year'].iloc[0])
        print('\nMost common year of birth: {}'.format(common_birth_year))
        print('\nMost recent year of birth: {}'.format(recent_birth_year))
        print('\nEarliest year of birth data entry: {}'.format(earliest_birth_year))

    print_times(start_time)

def print_times(start_time):
    """" Prints data analysis timer """
    print("---")
    print("This took %s seconds." % (time.time() - start_time))
    print("---")

def print_title(title):
    """" Prints section title """
    print('-'*50)
    print(title)
    print('-'*50)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        see_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

def see_data(df):
    """ prompts user to see individual data, fetches row records, and prints them """
    while True:
        see_data = input('\nDo you want to see an example of raw bikeshare data? Enter "yes or "no\n')
        if see_data.lower() != 'yes':
            break
        else:
            records = df.head(8).to_dict('records')
            for record in records:
                # print data in nice format
                print("{")
                print_pretty(record)
                print("}\n")
            break

def print_pretty(d, indent=0):
    """ print data in easily readable way """
    for key, value in d.items():
        print("  {}: {}".format(key, value))

if __name__ == "__main__":
	main()
