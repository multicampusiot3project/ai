<table>
    <tr>
        <td style="text-align:center;"
            bgcolor="#FFFFFF">Resnet50</td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">1e-3</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">1e-4</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">1e-5</span></td>
    </tr>
    <tr>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">lamb</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 혜주 c(a)</td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">-</span> 지연 a</td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 혜주 c(d)</td>
    </tr>
    <tr>
        <td  style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">adam</td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 혜주 c(a)</td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 지연 a
        		<br> E [22] T : [0.01547] V : [0.00182]</td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> 혜주</td>
    </tr>
    <tr>
        <td  style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">rmsprop</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 혜주 c(a)</td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 지연 a
        		<br> E [23] T : [0.01033] V : [0.00154] </td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">-</span> 지연c(5)</td>
    </tr>
    <tr>
        <td  style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">nadam</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 지연 c(1)
        		<br> E [20] T : [0.02579] V : [0.00320]</td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 지연 a
        		<br> E [20] T : [0.00953] V : [0.00164]</td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">-</span> 지연c(1)</td>
    </tr>
</table>

<table>
    <tr>
        <td style="text-align:center;"
            bgcolor="#FFFFFF">EfficientNet</td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">1e-3</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">1e-4</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">1e-5</span></td>
    </tr>
    <tr>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">lamb</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 혜주 c(b)</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 혜주 c(e)</span></td>
    </tr>
    <tr>
        <td  style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">adam</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 혜주 c(b)</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
    </tr>
    <tr>
        <td  style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">rmsprop</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
    </tr>
    <tr>
        <td  style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">nadam</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">-</span> 지연 c(4)</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
		<td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
    </tr>
</table>

<table>
    <tr>
        <td style="text-align:center;"
            bgcolor="#FFFFFF">Regnet</td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">1e-3</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">1e-4</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">1e-5</span></td>
    </tr>
    <tr>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">lamb</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 혜주 c(c)</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 혜주 lo</span></td>
    </tr>
    <tr>
        <td  style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">adam</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 혜주 c(c)</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:red">O</span> 혜주 lo</span></td>
    </tr>
    <tr>
        <td  style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">rmsprop</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
		<td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">-</span> 혜주</span></td>
    </tr>
    <tr>
        <td  style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">nadam</span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
		<td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
        <td style="text-align:center;"
            bgcolor="#FFFFFF"><span style="color:black">X</span> </span></td>
    </tr>
</table>











| resnet50 | 1e-3                                                         | 1e-4                                       | 1e-5                                           |
| -------- | ------------------------------------------------------------ | ------------------------------------------ | ---------------------------------------------- |
| lamb     | **<span style="color:red">o</span> 혜주 c(a)**               | - 지연a                                    | **<span style="color:red">o</span> 혜주 c(d)** |
| adam     | **<span style="color:red">o</span> 혜주 c(a)**               | **<span style="color:red">o</span> 지연a** | x 혜주                                         |
| rmsprop  | **<span style="color:red">o</span> 혜주 c(a)**               | **<span style="color:red">o</span> 지연a** | - 지연c(5)                                     |
| nadam    | **<span style="color:red">o</span> 지연 c(1)** 30e 0.191tl 0.141vl | **<span style="color:red">o</span> 지연a** | - 지연c(1)                                     |

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

