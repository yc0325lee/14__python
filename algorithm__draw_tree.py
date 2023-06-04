# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : algorithm__draw_tree.py
# - author : yc0325lee
# - created : 2022-11-04 21:37:02 by lee2103
# - modified : 2022-11-06 23:24:42 by yc032
# - description : 
# ----------------------------------------------------------------------------
#import collections
#nodeStack = collections.deque()
#indentStack = collections.deque()

nodeStack = list()
indentStack = list()

def __is_root_node():
    return len(nodeStack) == 1
def __is_leaf_node(node):
    return len(node) == 0 # if there's no child!
def __depth():
    return len(nodeStack)-1

def visit_node(parentNode, thisNode, thisName, rank):
    if len(indentStack) > 0:
        print(''.join([*indentStack[:-1], '+---', thisName]))
        #              -----------------   -----
        #                 unpack list      use this when print child-name
        #                                  instead of '|   '
        if( rank == len(parentNode)-1 ):
            indentStack[-1] = '    ' # we don't need '|    ' for child any more!
    else:
        print(thisName) # root-node!

    nodeStack.append(thisNode) # ---------------------------------------
    indentStack.append('|   ') # (1) if there are more children,
                               #     the latest indent should be '|   '.
                               # (2) if there's no child
                               #     the latest indent should be '    '.
                               # ---------------------------------------

    for i, childName in enumerate(thisNode.keys()):
        print(''.join(indentStack)) # joined-indent between nodes
        visit_node(thisNode, thisNode[childName], childName, i)
        #          ----+---  ---------+---------  ----+----  +
        #              |              |               |      i-th child
        #              |              |               node-name
        #              |              node
        #              parent-node

    indentStack.pop()
    nodeStack.pop()

    if len(indentStack) == 0:
        print() # newline at the end of output


hierarchy = {
    'Shape__Common' : {
        'Shape__Base' : {
            'Shape__OneDimensional' : {
                'Shape__Dot' : {},
                'Shape__Line' : {},
            },
            'Shape__TwoDimensional' : {
                'Shape__Circle' : {},
                'Shape__Square' : {},
                'Shape__Triangle' : {},
            },
            'Shape__ThreeDimensional' : {
                'Shape__Sphere' : {},
                'Shape__Cube' : {},
                'Shape__Cylinder' : {},
                'Shape__Tetrahedron' : {},
            },
        },
    },

    'UniversityMember' : {
        'Employee' : {
            'Faculty' : {
                'Administrator' : {
                    'AdministratorTeacher' : {},
                },
                'Teacher' : {
                    'AdministratorTeacher' : {},
                },
            },
            'Staff' : {},
        },
        'Student' : {
            'GraduateStudent' : {
                'DoctoralStudent' : {},
                'MastersStudent' : {},
            },
            'UndergraduateStudent' : {
                'Freshman' : {},
                'Junior' : {},
                'Senior' : {},
                'Sophomore' : {},
            },
        },
        'Alumnus' : {},
    },

    'Meridian__Common' : {
        'Meridian__RuleBase' : {
            'Meridian__SinglePathRule' : {
                'Meridian__CNTL' : {},
                'Meridian__DATA' : {},
                'Meridian__W_CNTL' : {},
                'Meridian__W_DATA' : {},
            },
            'Meridian__MultiPathRule' : {
                'Meridian__INTERFACE' : {},
                'Meridian__U_INTERFACE' : {},
                'Meridian__W_INTERFACE' : {},
                'Meridian__W_GLITCH' : {},
                'Meridian__W_RECON_GROUPS' : {},
            },
        },
    },
}


if __name__ == "__main__":
    import pprint

    #for rootName in hierarchy.keys():
    #    visit_node(hierarchy, hierarchy[rootName], rootName, 0)

    print('\n# shape hierarchy')
    visit_node(hierarchy, hierarchy['Shape__Common'], 'Shape__Common', 0)
    #          ---------  --------------------------  ---------------  -
    #          parentNode          thisNode               thisName     rank

    print('\n# UniversityMember hierarchy')
    visit_node(hierarchy, hierarchy['UniversityMember'], 'UniversityMember', 0)
    #          ---------  -----------------------------  ------------------  -
    #          parentNode           thisNode                   thisName      rank

    print('\n# MeridianRule hierarchy')
    visit_node(hierarchy, hierarchy['Meridian__Common'], 'Meridian__Common', 0)
    #          ---------  -----------------------------  ------------------  -
    #          parentNode           thisNode                   thisName      rank


    # debug
    pprint.pprint(hierarchy, indent=4)



# -------------------------------------
# Shape__Common
# |   
# +---Shape__Base
#     |   
#     +---Shape__OneDimensional
#     |   |   
#     |   +---Shape__Dot
#     |   |   
#     |   +---Shape__Line
#     |   
#     +---Shape__TwoDimensional
#     |   |   
#     |   +---Shape__Circle
#     |   |   
#     |   +---Shape__Square
#     |   |   
#     |   +---Shape__Triangle
#     |   
#     +---Shape__ThreeDimensional
#         |   
#         +---Shape__Sphere
#         |   
#         +---Shape__Cube
#         |   
#         +---Shape__Cylinder
#         |   
#         +---Shape__Tetrahedron


# -------------------------------------
# UniversityMember
# |   
# +---Employee
# |   |   
# |   +---Faculty
# |   |   |   
# |   |   +---Administrator
# |   |   |   |   
# |   |   |   +---AdministratorTeacher
# |   |   |   
# |   |   +---Teacher
# |   |       |   
# |   |       +---AdministratorTeacher
# |   |   
# |   +---Staff
# |   
# +---Student
# |   |   
# |   +---GraduateStudent
# |   |   |   
# |   |   +---DoctoralStudent
# |   |   |   
# |   |   +---MastersStudent
# |   |   
# |   +---UndergraduateStudent
# |       |   
# |       +---Freshman
# |       |   
# |       +---Junior
# |       |   
# |       +---Senior
# |       |   
# |       +---Sophomore
# |   
# +---Alumnus


# -------------------------------------
# Meridian__Common
# |   
# +---Meridian__RuleBase
#     |   
#     +---Meridian__SinglePathRule
#     |   |   
#     |   +---Meridian__CNTL
#     |   |   
#     |   +---Meridian__DATA
#     |   |   
#     |   +---Meridian__W_CNTL
#     |   |   
#     |   +---Meridian__W_DATA
#     |   
#     +---Meridian__MultiPathRule
#         |   
#         +---Meridian__INTERFACE
#         |   
#         +---Meridian__U_INTERFACE
#         |   
#         +---Meridian__W_INTERFACE
#         |   
#         +---Meridian__W_GLITCH
#         |   
#         +---Meridian__W_RECON_GROUPS
