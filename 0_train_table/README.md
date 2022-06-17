# Train Table

AI hub dessert 14개 항목 train 각 114장, valid 각 15장 data 학습



<table>
<thead>
  <tr>
    <th>resnet50</th>
    <th>1.00E-03</th>
    <th>1.00E-04</th>
    <th>1.00E-05</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">lamb</td>
    <td>혜주 c(a) <br>    E [32] LR [9.5677e-04] <br>     T : [0.04888] V : [0.02917]</td>
    <td>지연a <br>E [50] LR [2.5000e-05]<br>T : [0.19234] V : [0.11658]</td>
    <td>혜주 c(d)     <br>E [50] LR [2.5000e-06] <br><br>     T : [2.39901] V : [2.34901]</td>
  </tr>
  <tr>
    <td>0.709677419</td>
    <td>0.64516129</td>
    <td>0.129032258</td>
  </tr>
  <tr>
    <td rowspan="2">adam</td>
    <td>혜주 c(a)     <br>E [29] LR [9.8907e-04] <br>     T : [0.33711] V : [0.14360]</td>
    <td>지연a <br>E [22] LR [4.4774e-05]<br>T : [0.01547] V : [0.00182]</td>
    <td>혜주 c(a)     <br>E [50] LR [2.5000e-06] <br>     T : [0.01373] V : [0.00907]</td>
  </tr>
  <tr>
    <td>0.35483871</td>
    <td>0.419354839</td>
    <td>0.677419355</td>
  </tr>
  <tr>
    <td rowspan="2">rmsprop</td>
    <td>혜주 c(a)     <br>E [26] LR [8.3457e-04] <br>     T : [0.33711] V : [0.62680]</td>
    <td>지연a <br>E [23] LR [5.5226e-05] <br>T : [0.01033] V : [0.00154]</td>
    <td>지연c(5) <br>E [47] LR [4.3227e-07]<br>T : [0.01120] V : [0.00361]</td>
  </tr>
  <tr>
    <td>0.193548387</td>
    <td>0.677419355</td>
    <td>0.548387097</td>
  </tr>
  <tr>
    <td rowspan="2">nadam</td>
    <td>지연 c(1) <br>     E [20] LR [2.5000e-04]   <br>     T : [0.02579] V : [0.00320]</td>
    <td>지연a <br>E [20] LR [2.5000e-05] <br>T : [0.00953] V : [0.00164]</td>
    <td>지연c(1) <br>E [45] LR [0.0000e+00]<br>T : [0.01986] V : [0.00659]</td>
  </tr>
  <tr>
    <td>0.290322581</td>
    <td>0.64516129</td>
    <td>0.612903226</td>
  </tr>
</tbody>
</table>


<table>
<thead>
  <tr>
    <th>efficientnet</th>
    <th>1.00E-03</th>
    <th>1.00E-04</th>
    <th>1.00E-05</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">lamb</td>
    <td>혜주 c(b)     <br>E [49] LR [1.6543e-04] <br>     T : [0.00425] V : [0.00020]</td>
    <td>지연a <br>E [50] RL [2.5000e-05]<br>T : [1.61274] V : [1.53337]</td>
    <td>혜주 c(e)</td>
  </tr>
  <tr>
    <td>0.677419355</td>
    <td>0.419354839</td>
    <td>예정</td>
  </tr>
  <tr>
    <td rowspan="2">adam</td>
    <td>혜주 c(b)     <br>E [21] LR [3.4549e-04] <br>     T : [0.00800] V : [0.03702]</td>
    <td>지연a <br>E [41] LR [1.6543e-05]<br>T : [0.01585] V : [0.00052]</td>
    <td>혜주 c(c)</td>
  </tr>
  <tr>
    <td>0.709677419</td>
    <td>0.677419355</td>
    <td>예정</td>
  </tr>
  <tr>
    <td rowspan="2">rmsprop</td>
    <td>o 지연 c(4) <br>E [22] LR [4.4774e-04] <br>T : [0.01246] V : [0.00005]</td>
    <td>지연a <br>E [11] LR [1.6543e-05]<br>T : [0.04431] V : [0.00820]</td>
    <td>혜주 c(c)<br>     E [50] LR [2.5000e-06] <br>     T : [0.35883] V : [0.30719]</td>
  </tr>
  <tr>
    <td>0.677419355</td>
    <td>0.64516129</td>
    <td>0.612903226</td>
  </tr>
  <tr>
    <td rowspan="2">nadam</td>
    <td>o 지연c(4) <br>E [23] LR [5.5226e-04] <br>T : [0.00577] V : [0.00002]</td>
    <td>지연a <br>E [32] LR [9.5677e-05]<br>T : [0.02422] V : [0.00243]</td>
    <td>혜주 c(a)     <br>E [47] LR [4.3227e-07] <br>     T : [0.25645] V : [0.13758]</td>
  </tr>
  <tr>
    <td>0.64516129</td>
    <td>0.677419355</td>
    <td>0.580645161</td>
  </tr>
</tbody>
</table>


<table>
<thead>
  <tr>
    <th>regnet  </th>
    <th>1.00E-03</th>
    <th>1.00E-04</th>
    <th>1.00E-05</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">lamb</td>
    <td>혜주 c(c) <br>E [22] LR [4.4774e-04] <br>T : [0.01328] V : [0.00028]</td>
    <td> 지연a<br>E [50] LR [2.5000e-05]<br>T : [0.13482] V : [0.05515] </td>
    <td> o 혜주 lo <br>E [49] LR [1.6543e-06] <br>T : [2.29275] V : [2.20633]</td>
  </tr>
  <tr>
    <td>0.903225806</td>
    <td>0.612903226</td>
    <td>0.387096774</td>
  </tr>
  <tr>
    <td rowspan="2">adam</td>
    <td>혜주 c(c) <br>E [20] LR [2.5000e-04] <br>T : [0.01653] V : [0.13758]</td>
    <td> 지연a<br>E [22] LR [4.4774e-05] <br>T : [0.00371] V : [0.00040] </td>
    <td> o 혜주 lo <br>E [50] LR [2.5000e-06] <br>T : [0.00674] V : [0.00040]</td>
  </tr>
  <tr>
    <td>0.612903226</td>
    <td>0.838709677</td>
    <td>0.838709677</td>
  </tr>
  <tr>
    <td rowspan="2">rmsprop</td>
    <td>지연 c(8)        </td>
    <td> 지연a<br>E [21] LR [3.4549e-05]<br>T : [0.00424] V : [0.00034] </td>
    <td> o 혜주 lo <br>E [46] LR [1.0926e-07] <br>T : [0.00190] V : [0.00018]</td>
  </tr>
  <tr>
    <td>예정</td>
    <td>0.677419355</td>
    <td>0.935483871</td>
  </tr>
  <tr>
    <td rowspan="2"> nadam</td>
    <td>지연 c(1) </td>
    <td> 지연c(5)<br>E [24] LR [6.5451e-05]<br>T : [0.01436] V : [0.00030] </td>
    <td> o 혜주 lo<br>E [49] LR [1.6543e-06] <br>T : [0.00528] V : [0.00050] </td>
  </tr>
  <tr>
    <td>예정</td>
    <td>0.709677419</td>
    <td>0.870967742</td>
  </tr>
</tbody>
</table>
