from flask import *
import joblib


app = Flask(__name__)


def preprocess_occupation(Occupation):
    Occupation_Accountants = 0
    Occupation_Cleaning_staff = 0
    Occupation_Cooking_staff = 0
    Occupation_Core_staff = 0
    Occupation_Drivers = 0
    Occupation_HR_staff = 0
    Occupation_High_skill_tech_staff = 0
    Occupation_IT_staff = 0
    Occupation_Laborers = 0
    Occupation_Low_skill_Laborers = 0
    Occupation_Managers = 0 
    Occupation_Medicine_staff = 0
    Occupation_Private_service_staff = 0
    Occupation_Realty_agents = 0
    Occupation_Sales_staff = 0
    Occupation_Secretaries = 0
    Occupation_Security_staff  = 0
    Occupation_Unknown = 0
    Occupation_Waiters_barmen_staff = 0
    
    if Occupation == 'Accountants':
        Occupation_Accountants = 1
    elif Occupation  == 'Cleaning staff':
         Occupation_Cleaning_staff = 1
    elif Occupation  == 'Cooking staff':
         Occupation_Cooking_staff = 1
    elif Occupation  == 'Core staff':
         Occupation_Core_staff = 1
    elif Occupation  == 'Drivers':
         Occupation_Drivers = 1  
    elif Occupation  == 'HR staff':
         Occupation_HR_staff = 1
    elif Occupation  == 'High skill tech staff':
         Occupation_High_skill_tech_staff = 1
    elif Occupation  == 'IT staff':
         Occupation_IT_staff = 1
    elif Occupation  == 'Laborers':
         Occupation_Laborers = 1
    elif Occupation  == 'Low-skill Laborers ':
         Occupation_Low_skill_Laborers = 1
    elif Occupation  == 'Managers':
         Occupation_Managers = 1
    elif Occupation  == 'Medicine staff':
         Occupation_Medicine_staff  = 1
    elif Occupation  == 'Private service staff':
         Occupation_Private_service_staff = 1
    elif Occupation  == 'Realty agents':
         Occupation_Realty_agents = 1
    elif Occupation  == 'Sales staff':
         Occupation_Sales_staff = 1
    elif Occupation  == 'Secretaries':
         Occupation_Secretaries = 1
    elif Occupation  == 'Security staff':
         Occupation_Security_staff = 1
    elif Occupation  == 'Waiters/barmen staff':
         Occupation_Waiters_barmen_staff = 1
    

    return Occupation_Accountants, Occupation_Cleaning_staff, Occupation_Cooking_staff, Occupation_Core_staff, Occupation_Drivers, Occupation_HR_staff, Occupation_High_skill_tech_staff, Occupation_IT_staff, Occupation_Laborers, Occupation_Low_skill_Laborers, Occupation_Managerr, Occupation_Medicine_staff, Occupation_Private_service_staff, Occupation_Realty_agents, Occupation_Sales_staff, Occupation_Secretaries, Occupation_Security_staff, Occupation_Unknown, Occupation_Waiters_barmen_staff   



def preprocess_organization(Organization):
    Organization_Advertising = 0            
    Organization_Agriculture = 0            
    Organization_Bank = 0                   
    Organization_Business_Entity_Type_1 = 0 
    Organization_Business_Entity_Type_2 = 0
    Organization_Business_Entity_Type_3 = 0
    Organization_Cleaning = 0                
    Organization_Construction = 0           
    Organization_Culture = 0                
    Organization_Electricity = 0            
    Organization_Emergency = 0              
    Organization_Government  = 0            
    Organization_Hotel = 0                  
    Organization_Housing = 0                 
    Organization_Industry_type_1  = 0       
    Organization_Industry_type_10  = 0     
    Organization_Industry_type_11  = 0     
    Organization_Industry_type_12  = 0     
    Organization_Industry_type_13  = 0     
    Organization_Industry_type_2  = 0      
    Organization_Industry_type_3  = 0      
    Organization_Industry_type_4 = 0       
    Organization_Industry_type_5 = 0       
    Organization_Industry_type_6 = 0       
    Organization_Industry_type_7 = 0       
    Organization_Industry_type_8 = 0      
    Organization_Industry_type_9 = 0       
    Organization_Insurance = 0              
    Organization_Kindergarten  = 0          
    Organization_Legal_Services = 0         
    Organization_Medicine  = 0              
    Organization_Military = 0               
    Organization_Mobile  = 0                
    Organization_Other  = 0                 
    Organization_Police  = 0                
    Organization_Postal  = 0                
    Organization_Realtor = 0                
    Organization_Religion = 0               
    Organization_Restaurant = 0             
    Organization_School  = 0               
    Organization_Security  = 0              
    Organization_Security_Ministries = 0     
    Organization_Self_employed = 0          
    Organization_Services = 0              
    Organization_Telecom  = 0                
    Organization_Trade_type_1  = 0         
    Organization_Trade_type_2  = 0         
    Organization_Trade_type_3  = 0         
    Organization_Trade_type_4  = 0        
    Organization_Trade_type_5  = 0        
    Organization_Trade_type_6  = 0         
    Organization_Trade_type_7  = 0         
    Organization_Transport_type_1 = 0      
    Organization_Transport_type_2 = 0       
    Organization_Transport_type_3 = 0     
    Organization_Transport_type_4 = 0      
    Organization_University = 0             
    Organization_XNA = 0                    


    if Organization == 'Advertising':
        Organization_Advertising = 1
    elif Organization == 'Agriculture':
            Organization_Agriculture = 1
    elif Organization == 'Bank':
            Organization_Bank = 1
    elif Organization == 'Business Entity Type 1':
            Organization_Business_Entity_Type_1 = 1
    elif Organization == 'Business Entity Type 2':
            Organization_Business_Entity_Type_2 = 1
    elif Organization == 'Business Entity Type 3':
            Organization_Business_Entity_Type_3 = 1
    elif Organization == 'Cleaning':
            Organization_Cleaning = 1
    elif Organization == 'Construction':
            Organization_Construction = 1
    elif Organization == 'Culture':
            Organization_Culture = 1
    elif Organization == 'Electricity':
            Organization_Electricity   = 1
    elif Organization == 'Emergency':
            Organization_Emergency= 1
    elif Organization == 'Government':
            Organization_Government = 1
    elif Organization == 'Hotel':
            Organization_Hotel  = 1
    elif Organization == 'Housing':
            Organization_Housing  = 1
    elif Organization == 'Industry: type 1':
            Organization_Industry_type_1 = 1
    elif Organization == 'Industry: type 10':
            Organization_Industry_type_10 = 1
    elif Organization == 'Industry: type 11':
            Organization_Industry_type_11 = 1
    elif Organization == 'Industry: type 12':
            Organization_Industry_type_12 = 1
    elif Organization == 'Industry: type 13':
            Organization_Industry_type_13 = 1
    elif Organization == 'Industry: type 2':
            Organization_Industry_type_2= 1
    elif Organization == 'Industry: type 3':
            Organization_Industry_type_3 = 1
    elif Organization == 'Industry: type 4':
            Organization_Industry_type_4 = 1
    elif Organization == 'Industry: type 5':
            Organization_Industry_type_5 = 1
    elif Organization == 'Industry: type 6':
            Organization_Industry_type_6 = 1
    elif Organization == 'Industry: type 7':
            Organization_Industry_type_7 = 1
    elif Organization == 'Industry: type 8':
            Organization_Industry_type_8 = 1
    elif Organization == 'Industry: type 9':
            Organization_Industry_type_9 = 1
    elif Organization == 'Insurance':
            Organization_Insurance = 1
    elif Organization == 'Kindergarten':
            Organization_Kindergarten  = 1
    elif Organization == 'Legal Services':
            Organization_Legal_Services = 1
    elif Organization == 'Medicine':
            Organization_Medicine = 1
    elif Organization == 'Military':
            Organization_Military = 1
    elif Organization == 'Mobile':
            Organization_Mobile = 1
    elif Organization == 'Other':
            Organization_Other = 1
    elif Organization == 'Police':
            Organization_Police = 1
    elif Organization == 'Postal':
            Organization_Postal= 1
    elif Organization == 'Realtor':
            Organization_Realtor = 1
    elif Organization == 'Religion':
            Organization_Religion  = 1
    elif Organization == 'Restaurant':
            Organization_Restaurant  = 1
    elif Organization == 'School':
            Organization_School  = 1
    elif Organization == 'Security':
            Organization_Security = 1
    elif Organization == 'Security Ministries':
            Organization_Security_Ministries = 1
    elif Organization == 'Self-employed':
            Organization_Self_employed = 1
    elif Organization == 'Services':
            Organization_Services  = 1
    elif Organization == 'Telecom':
            Organization_Telecom = 1
    elif Organization == 'Trade: type 1 ':
            Organization_Trade_type_1 = 1
    elif Organization == 'Trade: type 2':
            Organization_Trade_type_2 = 1
    elif Organization == 'Trade: type 3':
            Organization_Trade_type_3 = 1
    elif Organization == 'Trade: type 4':
            Organization_Trade_type_4 = 1
    elif Organization == 'Trade: type 5':
            Organization_Trade_type_5 = 1
    elif Organization == 'Trade: type 6':
            Organization_Trade_type_6 = 1
    elif Organization == 'Trade: type 7':
            Organization_Trade_type_7 = 1
    elif Organization == 'Transport: type 1':
            Organization_Transport_type_1 = 1
    elif Organization == 'Transport: type 2':
            Organization_Transport_type_2 = 1
    elif Organization == 'Transport: type 3':
            Organization_Transport_type_3 = 1
    elif Organization == 'Transport: type 4':
            Organization_Transport_type_4 = 1
    elif Organization == 'University':
            Organization_University  = 1
    elif Organization == 'XNA':
            Organization_XNA = 1

    return Organization_Advertising, Organization_Agriculture, Organization_Bank, Organization_Business_Entity_Type_1, Organization_Business_Entity_Type_2, Organization_Business_Entity_Type_3, Organization_Cleaning, Organization_Construction, Organization_Culture, Organization_Electricity, Organization_Emergency, Organization_Government, Organization_Hotel, Organization_Housing, Organization_Industry_type_1, Organization_Industry_type_10, Organization_Industry_type_11, Organization_Industry_type_12, Organization_Industry_type_13, Organization_Industry_type_2, Organization_Industry_type_3, Organization_Industry_type_4, Organization_Industry_type_5, Organization_Industry_type_6, Organization_Industry_type_7, Organization_Industry_type_8, Organization_Industry_type_9, Organization_Insurance, Organization_Kindergarten,  Organization_Legal_Services, Organization_Medicine, Organization_Military, Organization_Mobile, Organization_Other, Organization_Police, Organization_Postal, Organization_Realtor, Organization_Religion, Organization_Restaurant, Organization_School, Organization_Security, Organization_Security_Ministries, Organization_Self_employed, Organization_Services, Organization_Telecom, Organization_Trade_type_1, Organization_Trade_type_2, Organization_Trade_type_3, Organization_Trade_type_4, Organization_Trade_type_5, Organization_Trade_type_6, Organization_Trade_type_7, Organization_Transport_type_1, Organization_Transport_type_2, Organization_Transport_type_3, Organization_Transport_type_4, Organization_University, Organization_XNA                   


def preprocess_income(Income):
    Income_Businessman  = 0
    Income_Commercial_associate = 0
    Income_Maternity_leave = 0
    Income_Pensioner = 0
    Income_State_servant = 0
    Income_Student = 0
    Income_Unemployed = 0
    Income_Working = 0

    if Income == 'Businessman':
        Income_Businessman = 1
    elif Income == 'Commercial associate':
        Income_Commercial_associate = 1
    elif Income == 'Maternity leave':
        Income_Maternity_leave = 1
    elif Income == 'Pensioner':
        Income_Pensioner = 1
    elif Income == 'State servant':
        Income_State_servant = 1
    elif Income == 'Student':
        Income_Student = 1
    elif Income == 'Unemployed':
        Income_Unemployed = 1
    elif Income == 'Working':
        Income_Working = 1

    return Income_Businessman, Income_Commercial_associate, Income_Maternity_leave, Income_Pensioner, Income_State_servant, Income_Student, Income_Unemployed, Income_Working               


loaded_model = joblib.load('model_lr.pkl')


@app.route("/", methods=["GET", "POST"])
def index():
    
    str_prediction = ''
    
    if request.method == "POST":

        Days_Birth = int(request.form["DAYS_BIRTH"])
        Region_Rating   = int(request.form["REGION_RATING_CLIENT_W_CITY"])
        Reg_City_Not_Work_City = int(request.form["REG_CITY_NOT_WORK_CITY"])
        Flag_Phone   = int(request.form["FLAG_EMP_PHONE"])
        Reg_City_Not_Live_City      = int(request.form["REG_CITY_NOT_LIVE_CITY"])
        Flag_Document = int(request.form["FLAG_DOCUMENT_3"])
        EXT_Source_1 = float(request.form["EXT_SOURCE_1"])
        EXT_Source_2 = float(request.form["EXT_SOURCE_2"])
        EXT_Source_3 = float(request.form["EXT_SOURCE_3"])
        Days_Phone_Change = int(request.form["DAYS_LAST_PHONE_CHANGE"])
        Days_Employes = int(request.form["DAYS_EMPLOYED"])
        Days_Id_Publish = int(request.form["DAYS_ID_PUBLISH"])
        
        
        Occupation_Accountants, Occupation_Cleaning_staff, Occupation_Cooking_staff, Occupation_Core_staff, Occupation_Drivers, Occupation_HR_staff, Occupation_High_skill_tech_staff, Occupation_IT_staff, Occupation_Laborers, Occupation_Low_skill_Laborers, Occupation_Managerr, Occupation_Medicine_staff, Occupation_Private_service_staff, Occupation_Realty_agents, Occupation_Sales_staff, Occupation_Secretaries, Occupation_Security_staff, Occupation_Unknown, Occupation_Waiters_barmen_staff = preprocess_occupation(str(request.form["Occupation"]))
        
        Organization_Advertising, Organization_Agriculture, Organization_Bank, Organization_Business_Entity_Type_1, Organization_Business_Entity_Type_2, Organization_Business_Entity_Type_3, Organization_Cleaning, Organization_Construction, Organization_Culture, Organization_Electricity, Organization_Emergency, Organization_Government, Organization_Hotel, Organization_Housing, Organization_Industry_type_1, Organization_Industry_type_10, Organization_Industry_type_11, Organization_Industry_type_12, Organization_Industry_type_13, Organization_Industry_type_2, Organization_Industry_type_3, Organization_Industry_type_4, Organization_Industry_type_5, Organization_Industry_type_6, Organization_Industry_type_7, Organization_Industry_type_8, Organization_Industry_type_9, Organization_Insurance, Organization_Kindergarten,  Organization_Legal_Services, Organization_Medicine, Organization_Military, Organization_Mobile, Organization_Other, Organization_Police, Organization_Postal, Organization_Realtor, Organization_Religion, Organization_Restaurant, Organization_School, Organization_Security, Organization_Security_Ministries, Organization_Self_employed, Organization_Services, Organization_Telecom, Organization_Trade_type_1, Organization_Trade_type_2, Organization_Trade_type_3, Organization_Trade_type_4, Organization_Trade_type_5, Organization_Trade_type_6, Organization_Trade_type_7, Organization_Transport_type_1, Organization_Transport_type_2, Organization_Transport_type_3, Organization_Transport_type_4, Organization_University, Organization_XNA = preprocess_organtization(str(request.form["Organization"]))
        
        Income_Businessman, Income_Commercial_associate, Income_Maternity_leave, Income_Pensioner, Income_State_servant, Income_Student, Income_Unemployed, Income_Working = preprocess_income(str(request.form["Income"]))
          
        ls_data = [Region_Rating, Reg_City_Not_Work_City, Flag_Phone, Reg_City_Not_Live_City, Flag_Document, EXT_Source_3, EXT_Source_1, EXT_Source_2, Days_Phone_Change, \
                   Income_Businessman, Income_Commercial_associate, Income_Maternity_leave, Income_Pensioner, Income_State_servant, Income_Student, Income_Unemployed, Income_Working, \
                   Occupation_Accountants, Occupation_Cleaning_staff, Occupation_Cooking_staff, Occupation_Core_staff, Occupation_Drivers, Occupation_HR_staff, Occupation_High_skill_tech_staff, Occupation_IT_staff, Occupation_Laborers, Occupation_Low_skill_Laborers, Occupation_Managerr, Occupation_Medicine_staff, Occupation_Private_service_staff, Occupation_Realty_agents, Occupation_Sales_staff, Occupation_Secretaries, Occupation_Security_staff, Occupation_Unknown, Occupation_Waiters_barmen_staff, \
                   Organization_Advertising, Organization_Agriculture, Organization_Bank, Organization_Business_Entity_Type_1, Organization_Business_Entity_Type_2, Organization_Business_Entity_Type_3, Organization_Cleaning, Organization_Construction, Organization_Culture, Organization_Electricity, Organization_Emergency, Organization_Government, Organization_Hotel, Organization_Housing, Organization_Industry_type_1, Organization_Industry_type_10, Organization_Industry_type_11, Organization_Industry_type_12, Organization_Industry_type_13, Organization_Industry_type_2, Organization_Industry_type_3, Organization_Industry_type_4, Organization_Industry_type_5, Organization_Industry_type_6, Organization_Industry_type_7, Organization_Industry_type_8, Organization_Industry_type_9, Organization_Insurance, Organization_Kindergarten,  Organization_Legal_Services, Organization_Medicine, Organization_Military, Organization_Mobile, Organization_Other, Organization_Police, Organization_Postal, Organization_Realtor, Organization_Religion, Organization_Restaurant, Organization_School, Organization_Security, Organization_Security_Ministries, Organization_Self_employed, Organization_Services, Organization_Telecom, Organization_Trade_type_1, Organization_Trade_type_2, Organization_Trade_type_3, Organization_Trade_type_4, Organization_Trade_type_5, Organization_Trade_type_6, Organization_Trade_type_7, Organization_Transport_type_1, Organization_Transport_type_2, Organization_Transport_type_3, Organization_Transport_type_4, Organization_University, Organization_XNA, \
                  Days_Birth, Days_Employes, Days_Id_Publish]
        
        prediction_results = loaded_model.predict([ls_data])
        prediction_results = prediction_results[0]
        
        if prediction_results == 1:
            str_prediction = 'Nasabah tidak bisa membayar!'
        elif prediction_results == 0:
            str_prediction = 'Nasabah bisa bayar!'

        
    return render_template("index.html", str_prediction=str_prediction)

