lst = []
lst1 = ['more', 'than', 'five', 'items', 'ok']
n = len(lst1)
print(n)
print(lst1[0], " ", lst1[(n-1)//2], " ", lst1[n-1])
print("========================="*3, "\n")

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
n = len(it_companies)
print(it_companies[0], " ", it_companies[(n-1)//2], " ", it_companies[n-1])
it_companies.append('Netflix')
it_companies.insert(len(it_companies)//2, 'Wells Fargo')
print(it_companies)
it_companies[it_companies.index('Apple')] = it_companies[it_companies.index('Apple')].upper()
print(it_companies)

week0 = '#; '.join(it_companies)
print(week0)

print('TCS' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)

first_three = it_companies[:3]
print(first_three)
last_three = it_companies[-3:]
print(last_three)

middle_index = len(it_companies) // 2

if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle_index - 1: middle_index + 1]
else:
    middle_companies = it_companies[middle_index: middle_index + 1]

print(middle_companies)

del it_companies[0]

middle_index = len(it_companies) // 2

if len(it_companies) % 2 == 0:
    del it_companies[middle_index - 1: middle_index + 1]
else:
    del it_companies[middle_index]

print(it_companies)
del it_companies[-1]
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies

print("========================="*3, "\n")

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

full_stack_copy = full_stack.copy()
index = full_stack_copy.index('Redux') + 1
full_stack_copy.insert(index, 'Python')
full_stack_copy.insert(index + 1, 'SQL')

print(full_stack_copy)

print("========================="*3, "\n")

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("min: {}, max: {}".format(ages[0], ages[-1]))
ages.insert(0, ages[0])
ages.insert(-1, ages[-1])
print(ages)
middle_index = len(ages) // 2

if len(ages) % 2 == 0:
    print((ages[middle_index] + ages[middle_index - 1]) / 2)
else:
    print(ages[middle_index])

avg_age = sum(ages) / len(ages)
print("Average age: ", avg_age)
range = ages[-1] - ages[0]
print(range)
print(abs(ages[0] - avg_age))
print(abs(ages[-1] - avg_age))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

middle_index = len(countries) // 2

if len(countries) % 2 == 0:
    print(countries[middle_index-1: middle_index+1])
else:
    print(countries[middle_index])

first_half = countries[:middle_index + 1] if len(countries) % 2 != 0 else countries[:middle_index]
second_half = countries[middle_index + 1:] if len(countries) % 2 != 0 else countries[middle_index:]

print(len(first_half))
print(len(second_half))

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country1, country2, country3, *scandic_countries = countries
print(country1)
print(country2)
print(country3)
print(scandic_countries)