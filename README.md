<h1>Drowsiness Detection</h1> 

<h3>Introduction:</h3>

Drowsiness detection is a project built using Dlib and OpenCV with Python as a backend language.

<h3>Logic of project:</h3>

The project includes direct working with the 68 facial landmark detector and also the face detector of the Dlib library.

The 68 facial landmark detector is a robustly trained efficient detector which detects the points on the human face using which we determine whether the eyes are open or they are closed.

Thus, this project can be used to check whether a person is awake or is feeling drowsy or is sleeping.

Run the code and two pop-ups will open:

<ul>
  <li>Status window</li>
  <li>Face landmark window</li>
</ul>

![1](https://user-images.githubusercontent.com/95907977/170853870-29890ea3-f07b-4075-bdcd-64c80808ca54.png)




<h4>There are three statuses:</h4>

<ul>
  <li>Active:</li> 

![2](https://user-images.githubusercontent.com/95907977/170853875-af0337d6-73eb-4e65-9452-b677ea1ff13a.png)


  <li>Drowsy:</li>

![3](https://user-images.githubusercontent.com/95907977/170853879-5c457e08-704e-4823-bf6e-73fa7911947c.png)


  <li>Sleeping:</li>

![4](https://user-images.githubusercontent.com/95907977/170853885-27907eb4-ca88-4dd3-b911-a2cd9ffad4b2.png)

</ul>

<h3>Getting started:</h3>

Libraries/Tools required:
<ol>
  <li> Python version: 3.8.6</li>
  <li> OpenCV</li>
  <li> Dlib (version 19.19.0)</li>
  <li> Numpy</li>
  <li> face_utils</li>
</ol>


<h3>How it works:</h3>
<ul>
  <li>So, first I installed the libraries which are given above and these requirements are there in a file named “requirements.txt”.</li>
  <li>In this we are taking the ratio which is described as 'Sum of distances of vertical landmarks divided by twice the distance between horizontal landmarks'.</li>
  <li>After installing libraries, run ‘drowsinessDetection.py’ </li>
</ul>

<h3>Things to note:</h3>
<ul>
  <li>The ratio is dependent on the system so we have to configure the thresholds of sleeping,drowsy and active.</li>
  <li>I have used the dlib 19.19.0 version so I will suggest installing it on python 3.8 version.</li>
</ul>



