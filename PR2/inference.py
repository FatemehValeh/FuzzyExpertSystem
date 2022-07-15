import fuzzification as fuz


def rules(chest_pain, blood_pressure, cholesterol, blood_sugar, ecg, max_heart_rate, sport_activities, old_peak,
          thallium, gender, age):
    sick1, sick2, sick3, sick4, healthy = [], [], [], [], []
    # print(age['very_old'])
    chest_pain_fuz = fuz.ChestPain().chest_pain_fuzzification(chest_pain)
    blood_pressure_fuz = fuz.BloodPressure().blood_pressure_fuzzification(blood_pressure)
    cholesterol_fuz = fuz.Cholesterol().cholesterol_fuzzification(cholesterol)
    blood_sugar_fuz = fuz.BloodSugar().blood_sugar_fuzzification(blood_sugar)
    ecg_fuz = fuz.ECG().ecg_fuzzification(ecg)
    max_heart_rate_fuz = fuz.MaxHeartRate().max_heart_beat_fuzzification(max_heart_rate)
    sport_activities_fuz = fuz.SportActivities().sport_activities_fuzzification(sport_activities)
    old_peak_fuz = fuz.OldPeak().old_peak_fuzzification(old_peak)
    thallium_fuz = fuz.Thallium().thallium_fuzzification(thallium)
    gender_fuz = fuz.Gender().gender_fuzzification(gender)
    age_fuz = fuz.Age().age_fuzzification(age)

#   ----- rules -----
    # 1
    sick4.append(min(age_fuz['very_old'], chest_pain_fuz['atypical_anginal']))
    # 2
    sick4.append(min(max_heart_rate_fuz['high'], age_fuz['old']))
    # 3
    sick3.append(min(gender_fuz['male'], max_heart_rate_fuz['medium']))
    # 4
    sick2.append(min(gender_fuz['female'], max_heart_rate_fuz['medium']))
    # 5
    sick3.append(min(chest_pain_fuz['non_anginal_pain'], blood_pressure_fuz['high']))
    # 6
    sick2.append(min(chest_pain_fuz['typical_anginal'], max_heart_rate_fuz['medium']))
    # 7
    sick3.append(min(blood_sugar_fuz['true'], age_fuz['mild']))
    # 8
    sick2.append(min(blood_sugar_fuz['false'], blood_pressure_fuz['very_high']))
    # 9
    sick1.append(max(chest_pain_fuz['asymptomatic'], age_fuz['very_old']))
    # 10
    sick1.append(max(blood_pressure_fuz['high'], max_heart_rate_fuz['low']))
    # 11
    healthy.append(chest_pain_fuz['typical_anginal'])
    # 12
    sick1.append(chest_pain_fuz['atypical_anginal'])
    # 13
    sick2.append(chest_pain_fuz['non_anginal_pain'])
    # 14
    sick3.append(chest_pain_fuz['asymptomatic'])
    # 15
    sick4.append(chest_pain_fuz['asymptomatic'])
    # 16
    sick1.append(gender_fuz['female'])
    # 17
    sick2.append(gender_fuz['male'])
    # 18
    healthy.append(blood_pressure_fuz['low'])
    # 19
    sick1.append(blood_pressure_fuz['medium'])
    # 20
    sick2.append(blood_pressure_fuz['high'])
    # 21
    sick3.append(blood_pressure_fuz['high'])
    # 22
    sick4.append(blood_pressure_fuz['very_high'])
    # 23
    healthy.append(cholesterol_fuz['low'])
    # 24
    sick1.append(cholesterol_fuz['medium'])
    # 25
    sick2.append(cholesterol_fuz['high'])
    # 26
    sick3.append(cholesterol_fuz['high'])
    # 27
    sick4.append(cholesterol_fuz['very_high'])
    # 28
    sick2.append(blood_sugar_fuz['true'])
    # 29
    healthy.append(ecg_fuz['normal'])
    # 30
    sick1.append(ecg_fuz['normal'])
    # 31
    sick2.append(ecg_fuz['abnormal'])
    # 32
    sick3.append(ecg_fuz['hypertrophy'])
    # 33
    sick4.append(ecg_fuz['hypertrophy'])
    # 34
    healthy.append(max_heart_rate_fuz['low'])
    # 35
    sick1.append(max_heart_rate_fuz['medium'])
    # 36
    sick2.append(max_heart_rate_fuz['medium'])
    # 37
    sick3.append(max_heart_rate_fuz['high'])
    # 38
    sick4.append(max_heart_rate_fuz['high'])
    # 39
    sick2.append(sport_activities_fuz['ok'])
    # 40
    healthy.append(old_peak_fuz['low'])
    # 41
    sick1.append(old_peak_fuz['low'])
    # 42
    sick2.append(old_peak_fuz['terrible'])
    # 43
    sick3.append(old_peak_fuz['terrible'])
    # 44
    sick4.append(old_peak_fuz['risk'])
    # 45
    healthy.append(thallium_fuz['normal'])
    # 46
    sick1.append(thallium_fuz['normal'])
    # 47
    sick2.append(thallium_fuz['medium'])
    # 48
    sick3.append(thallium_fuz['high'])
    # 49
    sick4.append(thallium_fuz['high'])
    # 50
    healthy.append(age_fuz['young'])
    sick1.append(age_fuz['mild'])
    sick2.append(age_fuz['old'])
    sick3.append(age_fuz['old'])
    sick4.append(age_fuz['very_old'])

    sick1 = max(sick1)
    sick2 = max(sick2)
    sick3 = max(sick3)
    sick4 = max(sick4)
    healthy = max(healthy)

    return dict(sick1=sick1, sick2=sick2, sick3=sick3, sick4=sick4, healthy=healthy)

#
# if __name__ == '__main__':
#     print(rules(1,1,1,1,1,138,1,1,1,0,25))
