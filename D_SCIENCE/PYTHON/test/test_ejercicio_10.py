
import unittest

from ejercicio_10 import week_day_selector


class WeekDaySelector(unittest.TestCase):
    
    def test_week_day_selector_no_language_give(self):
        self.assertEqual(week_day_selector(1),'Lunes')
        self.assertEqual(week_day_selector(2),'Martes')
        self.assertEqual(week_day_selector(3),'Miércoles')
        self.assertEqual(week_day_selector(4),'Jueves')
        self.assertEqual(week_day_selector(5),'Viernes')
        self.assertEqual(week_day_selector(6),'Sábado')
        self.assertEqual(week_day_selector(7),'Domingo')
    
    def test_week_day_selector_esp_language_given(self):
        self.assertEqual(week_day_selector(1,'es'),'Lunes')
        self.assertEqual(week_day_selector(2,'es'),'Martes')
        self.assertEqual(week_day_selector(3,'es'),'Miércoles')
        self.assertEqual(week_day_selector(4,'es'),'Jueves')
        self.assertEqual(week_day_selector(5,'es'),'Viernes')
        self.assertEqual(week_day_selector(6,'es'),'Sábado')
        self.assertEqual(week_day_selector(7,'es'),'Domingo')
        
        
    def test_week_day_selector_eng_language_given(self):
        self.assertEqual(week_day_selector(1,'en'),'Monday')
        self.assertEqual(week_day_selector(2,'en'),'Tuesday')
        self.assertEqual(week_day_selector(3,'en'),'Wednesday')
        self.assertEqual(week_day_selector(4,'en'),'Thursday')
        self.assertEqual(week_day_selector(5,'en'),'Friday')
        self.assertEqual(week_day_selector(6,'en'),'Saturday')
        self.assertEqual(week_day_selector(7,'en'),'Sunday')
        
    def test_week_day_selector_eng_language_given(self):
        self.assertEqual(week_day_selector(1,'ger'),'Montag')
        self.assertEqual(week_day_selector(2,'ger'),'Dienstag')
        self.assertEqual(week_day_selector(3,'ger'),'Mittwoch')
        self.assertEqual(week_day_selector(4,'ger'),'Donnerstag')
        self.assertEqual(week_day_selector(5,'ger'),'Freitag')
        self.assertEqual(week_day_selector(6,'ger'),'Samstag')
        self.assertEqual(week_day_selector(7,'ger'),'Sonntag')
        
    def test_week_day_selector_wrong_number(self):
         with self.assertRaises(ValueError):
            week_day_selector(0)
         with self.assertRaises(ValueError):
            week_day_selector(9)

            
            


if __name__=='__main__':
    unittest.main()