myDict = {
    "Fast":"In a quick Manner",
    "Harry":"A Coder",
    "Marks":[1,3,7],
    "anotherDict":{
        "TV" : "A Electronic Box"
    },
    1:2

}
print(type(myDict.keys()))
print(myDict.values())
print(myDict.items())
updateDict = {
    "Lovish" : "Friend"
}
myDict.update(updateDict)
print(myDict)
