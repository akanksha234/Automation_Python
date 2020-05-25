from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
print( join( path_segment_1, path_segment_2, path_segment_3))

def myjoin(*args):
  initial_string = args[0]
  for _ in args[1:]:
    initial_string += _
  return initial_string


joined = myjoin("Hi!", " my name is Akansha. ", "I was wondering if you would like to have some coffee with me. :)")
print(joined)
