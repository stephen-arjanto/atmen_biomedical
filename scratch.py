#/////////////////////////////////////////////////////////////////
# from math import floor
# def sample(input, count):
#     output = []
#     sample_size = float(len(input)) / count
#     for i in range(count):
#         output.append(input[int(floor(i * sample_size))])
#     return output
# sample(inhalation, 25)
# sample(exhalation, 25)
#/////////////////////////////////////////////////////////////////

#/////////////////////////////////////////////////////////////////
# Algorithm to undersample the vector
# def spacing(input,count):
#     sample_size = float(len(input)) / count
#     return sample_size

# inhalation_spacing_size = spacing (inhalation,50)
# print('spacing size = ', inhalation_spacing_size)

# print('new_exhalation = ', new_exhalation)
# def undersample(input, interval):
#     output = []
#     index = 1
#     for i in input:
#         value = i + (inhalation_spacing_size*index-index)/1*(next(input)-i)
#         output.append(value)
#     return output
# undersample_inhalation = undersample(inhalation, 50)
#/////////////////////////////////////////////////////////////////