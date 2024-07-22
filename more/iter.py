class Friend:
    def __init__(self):
        self.friends=['amir','ali','asghar','hamid']

    def __iter__(self):
        # return iter(self.friends)
        return self.friends.__iter__() #if varibale is iterable we can call __iter__ method of it

    
    def __next__(self):
        copy_names=self.friends
        if copy_names:
            return copy_names.pop()
        else:
            raise StopIteration

bahman=Friend()
for friend in bahman:
    print(friend)
print('='*90)
print('first of iterator= ',next(bahman))

########################

# class Friend:
#     def __init__(self):
#         self.friends=['amir','ali','asghar','hamid']

#     def __iter__(self):
#         self.copy_names=self.friends
#         return self
    
#     def __next__(self):
        
#         if self.copy_names:
#             return self.copy_names.pop()
#         else:
#             raise StopIteration
        
# bahman=Friend()
# bahman_iter=iter(bahman)
# print(next(bahman_iter))