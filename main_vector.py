from playLA.Vector import Vector
if __name__ == "__main__":

    vec=Vector([5,2])
    print(len(vec))
    print("vec[0]={},vec[1]={}".format(vec[0],vec[1]))


    vec2=Vector([3,1])
    print("{}+{}={}".format(vec,vec2,vec+vec2))
    print("{}-{}={}".format(vec,vec2,vec-vec2))
    print("{}*{}={}".format(vec,3,vec*3))
    print("{}*{}={}".format(3,vec,3*vec))
    print("{}".format(vec.__pos__()))
    print("{}".format(vec.__neg__()))


    zero2=Vector.zero(2)
    print(zero2)

    print(vec.norm())
    print(vec.normalize())
    print(vec.normalize().norm())
    print(vec2.normalize().norm())





    try:
        zero2.normalize()
    except ZeroDivisionError:
        print('cannot normalize zero vector {}'.format(zero2))

    print(vec.dot(vec2))


    vec3 = Vector([0,0])
    print("{} == {}?{}".format(zero2,vec3,vec3==zero2))
    print("{} != {}?{}".format(zero2, vec3, vec3 != zero2))