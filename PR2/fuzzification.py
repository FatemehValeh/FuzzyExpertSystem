class Age:

    def young(self, x):
        res = 0
        if 0 < x <= 29:
            res = 1
        elif 29 < x <= 38:
            res = -0.111 * x + 4.222
        return res

    def mild(self, x):
        res = 0
        if 33 < x <= 38:
            res = 0.2 * x - 6.6
        elif 38 < x <= 45:
            res = -0.143 * x + 6.429
        return res

    def old(self, x):
        res = 0
        if 40 < x <= 48:
            res = 0.125 * x - 5.0
        elif 48 < x <= 58:
            res = -0.1 * x + 5.80
        return res

    def very_old(self, x):
        res = 1
        if 0 <= x <= 52:
            res = 0
        elif 52 < x <= 60:
            res = 0.125 * x - 6.50
        return res

    def age_fuzzification(self, x):
        young = self.young(x)
        mild = self.mild(x)
        old = self.old(x)
        very_old = self.very_old(x)
        res = dict(young=young, mild=mild, old=old, very_old=very_old)
        return res


class BloodPressure:

    def low(self, x):
        res = 0
        if 0 <= x <= 111:
            res = 1
        elif 111 < x <= 134:
            res = -0.043 * x + 5.826
        return res

    def medium(self, x):
        res = 0
        if 127 <= x <= 139:
            res = 0.083 * x - 10.583
        elif 139 < x <= 153:
            res = -0.071 * x + 10.929
        return res

    def high(self, x):
        res = 0
        if 142 <= x <= 157:
            res = 0.067 * x - 9.467
        elif 157 < x <= 172:
            res = -0.067 * x + 11.467
        return res

    def very_high(self, x):
        res = 1
        if 0 <= x <= 154:
            res = 0
        elif 154 < x <= 171:
            res = 0.059 * x - 9.059
        return res

    def blood_pressure_fuzzification(self, x):
        low = self.low(x)
        medium = self.medium(x)
        high = self.high(x)
        very_high = self.very_high(x)
        res = dict(low=low, medium=medium, high=high, very_high=very_high)
        return res


class BloodSugar:

    def very_high(self, x):
        res = 1
        if 0 <= x <= 105:
            res = 0
        elif 105 < x <= 120:
            res = 0.067 * x - 7.0
        else:
            res = 1
        return res

    def blood_sugar_fuzzification(self, x):
        true = self.very_high(x)
        false = 1 - self.very_high(x)
        return dict(true=true, false=false)


class Cholesterol:

    def low(self, x):
        res = 0
        if 0 <= x <= 151:
            res = 1
        elif 151 < x <= 197:
            res = -0.022 * x + 4.283
        return res

    def medium(self, x):
        res = 0
        if 188 <= x <= 215:
            res = 0.037 * x - 6.963
        elif 215 < x <= 250:
            res = -0.029 * x + 7.143
        return res

    def high(self, x):
        res = 0
        if 217 <= x <= 263:
            res = 0.022 * x - 4.717
        elif 263 < x <= 307:
            res = -0.023 * x + 6.977
        return res

    def very_high(self, x):
        res = 1
        if 0 <= x <= 281:
            res = 0
        elif 281 < x <= 347:
            res = 0.015 * x - 4.258
        return res

    def cholesterol_fuzzification(self, x):
        low = self.low(x)
        medium = self.medium(x)
        high = self.high(x)
        very_high = self.very_high(x)
        res = dict(low=low, medium=medium, high=high, very_high=very_high)
        return res


class MaxHeartRate:

    def low(self, x):
        res = 0
        if 0 <= x <= 100:
            res = 1
        elif 100 < x <= 141:
            res = -0.024 * x + 3.439
        return res

    def medium(self, x):
        res = 0
        if 111 <= x <= 152:
            res = 0.024 * x - 2.707
        elif 152 < x <= 194:
            res = -0.024 * x + 4.619
        return res

    def high(self, x):
        res = 1
        if 0 <= x <= 152:
            res = 0
        elif 152 < x <= 210:
            res = 0.017 * x - 2.621
        return res

    def max_heart_beat_fuzzification(self, x):
        low = self.low(x)
        medium = self.medium(x)
        high = self.high(x)
        res = dict(low=low, medium=medium, high=high)
        return res


class ECG:

    def normal(self, x):
        if -0.5 <= x <= 0:
            res = 1
        elif 0 < x <= 0.4:
            res = -2.5 * x + 1
        else:
            res = 0
        return res

    def abnormal(self, x):
        if 0.2 <= x < 1:
            res = 1.25 * x - 0.25
        elif 1 <= x < 1.8:
            res = -1.25 * x + 2.25
        else:
            res = 0
        return res

    def hypertrophy(self, x):
        if -0.5 <= x < 1.4:
            res = 0
        elif 1.4 <= x < 1.9:
            res = 2 * x - 2.8
        else:
            res = 1
        return res

    def ecg_fuzzification(self, x):
        normal = self.normal(x)
        abnormal = self.abnormal(x)
        hypertrophy = self.hypertrophy(x)
        res = dict(normal=normal, abnormal=abnormal, hypertrophy=hypertrophy)
        return res


class OldPeak:

    def low(self, x):
        if 0 <= x <= 1:
            res = 1
        elif 1 < x <= 2:
            res = -1.0 * x + 2.0
        else:
            res = 0
        return res


    def risk(self, x):
        if 1.5 <= x <= 2.8:
            res = 0.769 * x - 1.154
        elif 2.8 < x <= 4.2:
            res = -0.714 * x + 3.000
        else:
            res = 0
        return res

    def terrible(self, x):
        if 0 < x <= 2.5:
            res = 0
        elif 2.5 < x <= 4:
            res = 0.667 * x - 1.667
        else:
            res = 1
        return res

    def old_peak_fuzzification(self, x):
        low = self.low(x)
        risk = self.risk(x)
        terrible = self.terrible(x)
        return dict(low=low, risk=risk, terrible=terrible)

class Output:

    def sick1(self, x):
        if 0 <= x <= 0.25:
            res = 1
        elif 0.25 < x <= 1:
            res = 1.333 * x + 1.333
        else:
            res = 0
        return res

    def sick2(self, x):
        if 0 <= x <= 1:
            res = x
        elif 1 < x <= 2:
            res = -1.000 * x + 2.000
        else:
            res = 0
        return res

    def sick3(self, x):
        if 1 <= x <= 2:
            res = 1.000 * x - 1.000
        elif 2 < x <= 3:
            res = -1.000 * x + 3.000
        else:
            res = 0
        return res

    def sick4(self, x):
        if 2 <= x <= 3:
            res = 1.000 * x - 2
        elif 3 < x <= 4:
            res = -1.000 * x + 4.000
        else:
            res = 0
        return res

    def healthy(self, x):
        if 0 <= x <= 3:
            res = 0
        elif 3 < x <= 3.75:
            res = 1.333 * x - 4.000
        else:
            res = 1
        return res

class ChestPain:

    def typical_anginal(self, x):
        if x == 1:
            res = 1
        else:
            res = 0
        return res

    def atypical_anginal(self, x):
        if x == 2:
            res = 1
        else:
            res = 0
        return res

    def non_anginal_pain(self, x):
        if x == 3:
            res = 1
        else:
            res = 0
        return res

    def asymptomatic(self, x):
        if x == 4:
            res = 1
        else:
            res = 0
        return res

    def chest_pain_fuzzification(self, x):
        typical_anginal = self.typical_anginal(x)
        atypical_anginal = self.atypical_anginal(x)
        non_anginal_pain = self.non_anginal_pain(x)
        asymptomatic = self.asymptomatic(x)
        return dict(typical_anginal=typical_anginal, atypical_anginal=atypical_anginal, non_anginal_pain=non_anginal_pain,
                    asymptomatic=asymptomatic)


class SportActivities:

    def not_ok(self, x):
        if x == 0:
            res = 1
        else:
            res = 0
        return res

    def ok(self, x):
        if x == 1:
            res = 1
        else:
            res = 0
        return res

    def sport_activities_fuzzification(self,x):
        not_ok = self.not_ok(x)
        ok = self.ok(x)
        return dict(not_ok=not_ok, ok=ok)


class Thallium:

    def normal(self, x):
        if x == 3:
            res = 1
        else:
            res = 0
        return res

    def medium(self, x):
        if x == 6:
            res = 1
        else:
            res = 0
        return res

    def high(self, x):
        if x == 7:
            res = 1
        else:
            res = 0
        return res

    def thallium_fuzzification(self, x):
        normal = self.normal(x)
        medium = self.medium(x)
        high = self.high(x)
        return dict(normal=normal, medium=medium, high=high)

class Gender:

    def male(self, x):
        if x == 0:
            res = 1
        else:
            res = 0
        return res

    def female(self, x):
        if x == 1:
            res = 1
        else:
            res = 0
        return res

    def gender_fuzzification(self, x):
        male = self.male(x)
        female = self.female(x)
        return dict(male=male, female=female)


# if __name__ == '__main__':
    # foo = Age()
    # print(foo.age_fuzzification(40))
