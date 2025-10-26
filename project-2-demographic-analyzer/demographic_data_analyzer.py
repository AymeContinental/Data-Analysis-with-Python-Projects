import pandas as pd
import os
def calculate_demographic_data(print_data=True):
 
    # Esto obtiene la ruta de la carpeta DONDE ESTÁ el script .py
    script_dir = os.path.dirname(__file__) 
    # Esto une la ruta de la carpeta con el nombre del archivo CSV
    file_path = os.path.join(script_dir, 'adult.data.csv') 
    
    df = pd.read_csv(file_path)
    
    # ¿Cuántas personas de cada raza están representadas en este conjunto de datos?
    race_count = df['race'].value_counts()

    # ¿Cuál es la edad promedio de los hombres?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # ¿Cuál es el porcentaje de personas que tienen un título de Bachelor?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # ¿Qué porcentaje de personas con educación avanzada (Bachelors, Masters, o Doctorate) ganan más de 50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich_df = df[higher_education & (df['salary'] == '>50K')]
    higher_education_rich = round((higher_education_rich_df.shape[0] / df[higher_education].shape[0]) * 100, 1)

    # ¿Qué porcentaje de personas sin educación avanzada ganan más de 50K?
    lower_education = ~higher_education
    lower_education_rich_df = df[lower_education & (df['salary'] == '>50K')]
    lower_education_rich = round((lower_education_rich_df.shape[0] / df[lower_education].shape[0]) * 100, 1)

    # ¿Cuál es el número mínimo de horas que una persona trabaja por semana?
    min_work_hours = df['hours-per-week'].min()

    # ¿Qué porcentaje de las personas que trabajan el número mínimo de horas por semana tienen un salario de más de 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # ¿Qué país tiene el mayor porcentaje de personas que ganan >50K y cuál es ese porcentaje?
    country_stats = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    highest_earning_country_percentage = round(country_stats['>50K'].max() * 100, 1)
    highest_earning_country = country_stats['>50K'].idxmax()

    # Identificar la ocupación más popular para aquellos que ganan >50K en India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education earning >50K: {higher_education_rich}%")
        print(f"Percentage without higher education earning >50K: {lower_education_rich}%")
        print(f"Min work hours: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work min hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }