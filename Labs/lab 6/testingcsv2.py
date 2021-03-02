import pandas as pd

read_file = pd.read_csv('riskfactors.csv')
drop_file = read_file.drop(read_file.index[:5])

####### FIND MIN AND MAX ########## 
heart_disease = read_file.iloc[5:,1]
heart_min = heart_disease.min()
heart_max = heart_disease.max()

motor = read_file.iloc[5:,5]
motor_num = pd.to_numeric(motor)
motor_min = motor_num.min()
motor_max = motor_num.max()

teen_birth = read_file.iloc[5:,7]
birth_file_list = [x for x in teen_birth]
teen_num = pd.to_numeric(birth_file_list)
teen_min = teen_num.min()
teen_max = teen_num.max()

adult_smoking = read_file.iloc[5:,11]
adult_smoking = [i[:-2] for i in adult_smoking]
adult_num = pd.to_numeric(adult_smoking)
smoke_min = adult_num.min()
smoke_max = adult_num.max()

adult_obesity = read_file.iloc[5:,13]
obesity_file_list = [i[:-2] for i in adult_obesity]
obesity_num = pd.to_numeric(obesity_file_list)
obesity_min = obesity_num.min()
obesity_max = obesity_num.max()

###### GETTING INDEX for MIN #######################################
heart_disease_min_index = pd.Index(list(heart_disease))
heart_disease_min_index_loc = heart_disease_min_index.get_loc(heart_min)
motor_min_index = pd.Index(list(motor_num))
motor_min_index_loc = motor_min_index.get_loc(motor_min)
teen_birth_min_index = pd.Index(list(teen_num))
teen_birth_min_index_loc = teen_birth_min_index.get_loc(teen_min)
smoke_min_index = pd.Index(list(adult_num))
smoke_min_index_loc = smoke_min_index.get_loc(smoke_min)
obesity_min_index = pd.Index(list(obesity_num))
obesity_min_index_loc = obesity_min_index.get_loc(obesity_min)

####### GET NAMES OF MIN INDEX #########
heart_min_state = drop_file.iat[heart_disease_min_index_loc,0]
motor_min_state = drop_file.iat[motor_min_index_loc,0]
teen_birth_min_state = drop_file.iat[teen_birth_min_index_loc,0]
smoke_min_state = drop_file.iat[smoke_min_index_loc,0]
obesity_min_state = drop_file.iat[obesity_min_index_loc,0]

######## GETTING INDEX FOR MAX ##########
heart_disease_max_index = pd.Index(list(heart_disease))
heart_disease_max_index_loc = heart_disease_max_index.get_loc(heart_max)
motor_max_index = pd.Index(list(motor_num))
motor_max_index_loc = motor_max_index.get_loc(motor_max)
teen_birth_max_index = pd.Index(list(teen_num))
teen_birth_max_index_loc = teen_birth_max_index.get_loc(teen_max)
smoke_max_index = pd.Index(list(adult_num))
smoke_max_index_loc = smoke_max_index.get_loc(smoke_max)
obesity_max_index = pd.Index(list(obesity_num))
obesity_max_index_loc = obesity_max_index.get_loc(obesity_max)

####### GETTING NAMES OF MAX ###########
heart_max_state = drop_file.iat[heart_disease_max_index_loc,0]
motor_max_state = drop_file.iat[motor_max_index_loc,0]
teen_birth_max_state = drop_file.iat[teen_birth_max_index_loc,0]
smoke_max_state = drop_file.iat[smoke_max_index_loc,0]
obesity_max_state = drop_file.iat[obesity_max_index_loc,0]



def create_dataframe():
    data = [['Heart Disease Death Rate (2007)', heart_min_state, heart_min, heart_max_state, heart_max], 
            ['Motor Vehicle Death Rate (2009)', motor_min_state, motor_min, motor_max_state, motor_max],
            ['Teen Birth Rate (2009)', teen_birth_min_state, teen_min, teen_birth_max_state, teen_max], 
            ['Adult Smoking (2010)', smoke_min_state, smoke_min, smoke_max_state, smoke_max], 
            ['Adult Obesity (2010)', obesity_min_state, obesity_min, obesity_max_state, obesity_max]]
    data_frame = pd.DataFrame(data,columns=['Indicator', 'State', 'Minimum', 'State', 'Maximum'], dtype=float)

    data_frame.to_csv('cdctest3.csv')


def main():
    create_dataframe()


if __name__ == '__main__': main()