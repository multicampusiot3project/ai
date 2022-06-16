| resnet50 | 1e-3                                      | 1e-4                                       | 1e-5                                      |
| -------- | ----------------------------------------- | ------------------------------------------ | ----------------------------------------- |
| lamb     | **<span style="color:red">o</span> 혜주** | x 지연a                                    | **<span style="color:red">o</span> 혜주** |
| adam     | **<span style="color:red">o</span> 혜주** | **<span style="color:red">o</span> 지연a** | x 혜주                                    |
| rmsprop  | **<span style="color:red">o</span> 혜주** | **<span style="color:red">o</span> 지연a** | x 인후                                    |
| nadam    | x 지연c(1)                                | - 지연a                                    | x 인후                                    |

| efficientnet | 1e-3                                      | 1e-4 | 1e-5                                      |
| ------------ | ----------------------------------------- | ---- | ----------------------------------------- |
| lamb         | **<span style="color:red">o</span> 혜주** | x    | **<span style="color:red">o</span> 혜주** |
| adam         | **<span style="color:red">o</span> 혜주** | x    | x                                         |
| rmsprop      | x                                         | x    | x                                         |
| nadam        | - 지연c(4)                                        | x    | x                                         |

| regnet  | 1e-3                                      | 1e-4 | 1e-5                                      |
| ------- | ----------------------------------------- | ---- | ----------------------------------------- |
| lamb    | **<span style="color:red">o</span> 혜주** | x    | **<span style="color:red">o</span> 혜주** |
| adam    | **<span style="color:red">o</span> 혜주** | x    | **<span style="color:red">o</span> 혜주** |
| rmsprop | x                                         | x    | - 혜주                                    |
| nadam   | x                                         | x    | x                                         |

