| resnet50 | 1e-3                                      | 1e-4                                       | 1e-5                                      |
| -------- | ----------------------------------------- | ------------------------------------------ | ----------------------------------------- |
| lamb     | **<span style="color:red">o</span> 혜주 c(a)** | x 지연a                                    | **<span style="color:red">o</span> 혜주 c(d)** |
| adam     | **<span style="color:red">o</span> 혜주 c(a)** | **<span style="color:red">o</span> 지연a** | x 혜주                                    |
| rmsprop  | **<span style="color:red">o</span> 혜주 c(a)** | **<span style="color:red">o</span> 지연a** | x 인후                                    |
| nadam    | **<span style="color:red">o</span> 지연 c(1)**                                | - 지연a                                    | x 인후                                    |

| efficientnet | 1e-3                                      | 1e-4 | 1e-5                                      |
| ------------ | ----------------------------------------- | ---- | ----------------------------------------- |
| lamb         | **<span style="color:red">o</span> 혜주 c(b)** | x    | **<span style="color:red">o</span> 혜주 c(e)** |
| adam         | **<span style="color:red">o</span> 혜주 c(b)** | x    | x                                         |
| rmsprop      | x                                         | x    | x                                         |
| nadam        | - 지연c(4)                                        | x    | x                                         |

| regnet  | 1e-3                                      | 1e-4 | 1e-5                                      |
| ------- | ----------------------------------------- | ---- | ----------------------------------------- |
| lamb    | **<span style="color:red">o</span> 혜주 c(c)** | x    | **<span style="color:red">o</span> 혜주 lo** |
| adam    | **<span style="color:red">o</span> 혜주 c(c)** | x    | **<span style="color:red">o</span> 혜주 lo** |
| rmsprop | x                                         | x    | - 혜주                                    |
| nadam   | x                                         | x    | x                                         |

