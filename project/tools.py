def update_end_dates(self,events):
        start_year=int(self.start_year.get())
        start_month=int(self.start_month.get())
        start_day=int(self.start_day.get())
        end_year=int(self.end_year.get())
        end_month=int(self.end_month.get())
        end_day=int(self.end_day.get())
        valid_end_year=list(range(start_year,2025))
        self.end_year['values']=valid_end_year
        if end_year < start_year:
            self.end_year.set(start_year)
            
        if start_year == end_year:
            valid_end_month=list(range(start_month,13))
            self.end_month['values']=valid_end_month
            if end_month < start_month:
                self.end_month.set(start_month)
                
        if start_month == 2:
            self.start_day['values']=list(range(1,29))
            if start_day > 28:
                self.start_day.set(28)
        elif start_month in [4,6,9,11]:
            self.start_day['values']=list(range(1,31))
            if start_day > 30:
                    self.start_day.set(30)
        else:
            self.start_day['values']=list(range(1,32))
            
        if end_month == 2:
            self.end_day['values']=list(range(1,29))
            if end_day > 28:
                self.end_day.set(28)
        elif end_month in [4,6,9,11]:
            self.end_day['values']=list(range(1,31))
            if end_day > 30:
                self.end_day.set(30)
        else:
            self.end_day['values']=list(range(1,32))
            
        if start_year == end_year and start_month == end_month:
            if start_month == 2:
                valid_end_day=list(range(start_day,29))
                self.end_day['values']=valid_end_day
                if end_day > 28:
                    self.end_day.set(28)
            elif start_month in [4,6,9,11]:
                valid_end_day=list(range(start_day,31))
                self.end_day['values']=valid_end_day
                if end_day > 30:
                    self.end_day.set(30)
            else:
                valid_end_day=list(range(start_day,32))
                self.end_day['values']=valid_end_day
            if end_day < start_day:
                self.end_day.set(start_day)