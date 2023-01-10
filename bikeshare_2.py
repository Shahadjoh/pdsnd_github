import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv','new york city': 'new_york_city.csv','washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bike_share data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the city you would like to explore (chicago, new york city, washington): ")
    while city.lower() not in CITY_DATA:
        print("Invalid city. Please enter a valid city: ")
        city = input("Enter the city you would like to explore (chicago, new york city, washington): ").lower
    # get user input for month (all, january, february, ... , june)
    month = input("Enter the month you would like to filter by (all, january, february, ... , june): ")
    while month.lower() not in ["all", "january", "february", "march", "april", "may", "june"]:
        print("Invalid month. Please enter a valid month: ")
        month = input("Enter the month you would like to filter by (all, january, february, ... , june): ")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day of the week you would like to filter by (all, monday, tuesday, ... sunday): ")
    while day.lower() not in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
        print('Invalid day of the week. Please enter a valid day:')
        day = input("Enter the day of the week you would like to filter by (all, monday, tuesday, ... sunday): ")

    print('-' * 40)
    return city, month, day

def load_data(city,month,day):
    start_time = time.time()

    """Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(f"{city}.csv")
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_name'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df [df['month'] == month]
        # filter by day if applicable
        if day != 'all':
            # filter by day to create the new dataframe
            df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["month"].mode()
    if common_month is not None:
        common_month = common_month[0]
        print("Most Common Month:",common_month)
    else:
        print("There is no common month.")

    # display the most common day of week
    common_day = df['day_name'].mode()
    if common_day is not None:
        common_day = common_day[0]
        print('Most Common Day of Week:', common_day)
    else:
        print("There is no common day of week.")

    # display the most common start hour
    common_hour = df['hour'].mode()
    if common_hour is not None:
        common_hour = common_hour[0]
        print('Most Common Start Hour:', common_hour)
    else:
        print("There is no common start hour.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)
# display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['trip'].mode()[0]
    print('Most Frequent Trip:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    else:
        print("Gender data is not available.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("Earliest year of birth:", earliest_birth_year)
        print("Most recent year of birth:", most_recent_birth_year)
        print("Most common year of birth:", most_common_birth_year)
    else:
        print("Birth year data is not available right now.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
def name_user()
    print("inter your name")
    def printinfo()
    print("shahad")



def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0

    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        if start_loc >= len(df):
            print("No more rows to display")
            break
        view_data = input("Do you wish to continue?: ").lower()


if __name__ == "__main__":
      main()