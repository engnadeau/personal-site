---
abstract: |
  The use of robotics in medicine is of growing importance for modern health services, as robotic systems have the capacity to improve upon human tasks, thereby enhancing the treatment ability of a healthcare provider. In the medical sector, ultrasound imaging is an inexpensive approach without the high radiation emissions often associated with other modalities, especially when compared to MRI and CT imaging respectively. Over the past two decades, considerable effort has been invested into freehand ultrasound robotics research and development.

  However, this research has focused on the feasibility of the application, not the robotic fundamentals, such as motion control, calibration, and contextual awareness. Instead, much of the work is concentrated on custom designed robots, ultrasound image generation and visual servoing, or teleoperation. Research based on these topics often suffer from important limitations that impede their use in an adaptable, scalable, and real-world manner. Particularly, while custom robots may be designed for a specific application, commercial collaborative robots are a more robust and economical solution. Otherwise, various robotic ultrasound studies have shown the feasibility of using basic force control, but rarely explore controller tuning in the context of patient safety and deformable skin in an unstructured environment. Moreover, many studies evaluate novel visual servoing approaches, but do not consider the practicality of relying on external measurement devices for motion control. These studies neglect the importance of robot accuracy and calibration, which allow a system to safely navigate its environment while reducing the imaging errors associated with positioning. Hence, while the feasibility of robotic ultrasound has been the focal point in previous studies, there is a lack of attention to what occurs between system design and image output.

  This thesis addresses limitations of the current literature through three distinct contributions. Given the force-controlled nature of an ultrasound robot, the first contribution presents a closed-loop calibration approach using impedance control and low-cost equipment. Accuracy is a fundamental requirement for high-quality ultrasound image generation and targeting. This is especially true when following a specified path along a patient or synthesizing 2D slices into a 3D ultrasound image. However, even though most industrial robots are inherently precise, they are not necessarily accurate. While robot calibration itself has been extensively studied, many of the approaches rely on expensive and highly delicate equipment. Experimental testing showed that this method is comparable in quality to traditional calibration using a laser tracker. As demonstrated through an experimental study and validated with a laser tracker, the absolute accuracy of a collaborative robot was improved to a maximum error of 0.990mm, representing a 58.4% improvement when compared to the nominal model.

  The second contribution explores collisions and contact events, as they are a natural by-product of applications involving physical human-robot interaction (pHRI) in unstructured environments. Robot-assisted medical ultrasound is an example of a task where simply stopping the robot upon contact detection may not be an appropriate reaction strategy. Thus, the robot should have an awareness of body contact location to properly plan force-controlled trajectories along the human body using the imaging probe. This is especially true for remote ultrasound systems where safety and manipulability are important elements to consider when operating a remote medical system through a communication network. A framework is proposed for robot contact classification using the built-in sensor data of a collaborative robot. Unlike previous studies, this classification does not discern between intended vs. unintended contact scenarios, but rather classifies what was involved in the contact event. The classifier can discern different ISO/TS 15066:2016 specific body areas along a human-model leg with 89.37% accuracy. Altogether, this contact distinction framework allows for more complex reaction strategies and tailored robot behaviour during pHRI.

  Lastly, given that the success of an ultrasound task depends on the capability of the robot system to handle pHRI, pure motion control is insufficient. Force control techniques are necessary to achieve effective and adaptable behaviour of a robotic system in the unstructured ultrasound environment while also ensuring safe pHRI. While force control does not require explicit knowledge of the environment, to achieve an acceptable dynamic behaviour, the control parameters must be tuned. The third contribution proposes a simple and effective online tuning framework for force-based robotic freehand ultrasound motion control. Within the context of medical ultrasound, different human body locations have a different stiffness and will require unique tunings. Through real-world experiments with a collaborative robot, the framework tuned motion control for optimal and safe trajectories along a human leg phantom. The optimization process was able to successfully reduce the mean absolute error (MAE) of the motion contact force to 0.537N through the evolution of eight motion control parameters. Furthermore, contextual awareness through motion classification can offer a framework for pHRI optimization and safety through predictive motion behaviour with a future goal of autonomous pHRI. As such, a classification pipeline, trained using the tuning process motion data, was able to reliably classify the future force tracking quality of a motion session with an accuracy of 91.82 %.
aliases:
- /publication/nadeau-2019-towards
- /publication/2020/2/nadeau-2019-towards
authors:
- Nicholas A. Nadeau
date: "2020-02-25"
featured: false
publication: École de technologie supérieure
publication_types:
- "7"
publishDate: "2020-02-25"
tags:
- adaptive systems
- calibration
- evolutionary computation
- force control
- human-robot interaction
- medical robotics
- motion control
- optimization
- robot control
- robot kinematics
- robotics
- trajectory optimization
- ultrasonic imaging
- accuracy
- behaviour
- body
- calibration
- classification
- environment
- framework
- motion
- optimization
- robotics
- study
- system
- ultrasound
title: Towards the development of safe, collaborative robotic freehand ultrasound
url_pdf: http://espace.etsmtl.ca/id/eprint/2461
---
