import numpy as np


class ObjLoader:
    def __init__(self):
        self.v = []     # vertex coordinates
        self.vt = []    # texture coordinates
        self.vn = []    # normal coordinates
        self.f = []

        self.v_idx = []
        self.vt_idx = []
        self.vn_idx = []

        self.model = []

    def load_model(self, file):
        for line in open(file, 'r'):
            if line.startswith('#'):
                continue
            values = line.split()
            if not values:
                continue
            if values:
                # if values[0] == 'v':
                #     self.v.append(values[1:4])
                if values[0] == 'v':
                    vertex = np.array(values[1:], dtype=float)
                    self.v.append(vertex)
                if values[0] == 'vt':
                    self.vt.append(values[1:3])
                if values[0] == 'vn':
                    self.vn.append(values[1:4])

                if values[0] == 'f':
                    face = []
                    for k in range(1, len(values)):
                        face.append([int(s) for s in values[k].replace('//', '/').split('/')])
                    if len(face) > 3:  # triangulate the n-polynomial face, n>3
                        self.f.extend(
                            [[face[0][0] - 1, face[k][0] - 1, face[k + 1][0] - 1] for k in range(1, len(face) - 1)])
                    else:
                        self.f.append([face[j][0] - 1 for j in range(len(face))])
                else:
                    pass
            else:
                pass
            # if values[0] == 'f':
                # f_idx = []  # face indexes
                # t_idx = []  # texture indexes
                # n_idx = []  # normal indexes
                # for v in values[1:4]:
                #     w = v.split('/')
                #     f_idx.append(int(w[0])-1)
                #     t_idx.append(int(w[1])-1)
                #     n_idx.append(int(w[2])-1)
                # self.v_idx.append(f_idx)
                # self.vt_idx.append(t_idx)
                # self.vn_idx.append(n_idx)

                # for k in range(1, len(values)):
                #     self.f.append([int(s) for s in values[k].replace('//', '/').split('/')])
                # if len(self.f) > 3:
                #     self.f.extend(
                #         [[self.f[0][0] - 1, self.f[k][0] - 1, self.f[k + 1][0] - 1] for k in range(1, len(self.f) - 1)])
                # else:
                #     self.f.append([self.f[j][0] - 1 for j in range(len(self.f))])

        # self.v_idx = [y for x in self.v_idx for y in x]
        # self.vt_idx = [y for x in self.vt_idx for y in x]
        # self.vn_idx = [y for x in self.vn_idx for y in x]
        #
        # for i in self.v_idx:
        #     self.model.extend(self.v[i])
        #
        # for i in self.vt_idx:
        #     self.model.extend(self.vt[i])
        #
        # for i in self.vn_idx:
        #     self.model.extend(self.vn[i])

        self.model = np.array(self.model, dtype='float32')
