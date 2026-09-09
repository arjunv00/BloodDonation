

import mysql.connector




class BloodDonorManagement:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Arjunvinayak@123",
            database="blood_db",

        )
        print("Connected Successfully")

    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = ("insert into donor (name,blood_group,phone,city,last_donation) values (%s,%s,%s,%s,%s)")
            values =[v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Donor added Successfully")
        except Exception as e:
            print(e)

    def get(self):
            try:
                self.cursor = self.connection.cursor()
                query = "select * from donor"
                self.cursor.execute(query)
                record = self.cursor.fetchall()
                for data in record:
                    print(data)
            except Exception as e:
                print(e)

    def retrieve(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query = "select * from donor where id = %s"
            values=(id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            if record==None:
                print("Donor not found....")
            print(record)
        except Exception as e:
            print(e)


    def delete(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query ="select from donor where id =%s "
            values=(id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            if record != None:
                query = "delete from donor where id = %s"
                self.cursor.execute(query)
                self.connection.commit()
                print("Donor deleted Successfully")
            else:
                print("Donor not found...")
        except Exception as e:
            print(e)



    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor where id = %s"
            values=(id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return  None


    def put(self,id=None, **Kwargs):
        try:
            record=self.get_object(id=id)   #Check whether the record exists
            if record != None: # if a record is foumd , record will not be None
                self.cursor = self.connection.cursor()
                placeholder=""  # create an empty string
                #this variable  will be used to construct the SET part of the sql
                for k in Kwargs.keys():#name , blood_group,city....etc
                    placeholder += k +"=%s ," #Build the SET condition
                    # SET name="%s" , city+"%s", blood_group="%s".....etc
                    placeholder = placeholder.rstrip(", ") # Removes the last comma
                    query =f"update donor set {placeholder} where id =%s"
                    values = [v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    print("Donor details updated Successfully......")

            else:
                print("Donor not found.....")
        except Exception as e:
            print(e)




donner_instance = BloodDonorManagement()
#donner_instance.get()
#donner_instance.retrieve(id=1)
#donner_instance.post(name="arjun",blood_group="B+",phone="8848165742",city="kakkanadu",last_donation=datetime.today())
#donner_instance.delete(id=1)
#print("After deleting ")
#donner_instance.get()
#donner_instance.get_object()
donner_instance.put()

