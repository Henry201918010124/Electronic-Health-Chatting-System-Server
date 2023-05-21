"""
coding:utf-8
file: datas.py
@time: 2022/12/18 15:08
@desc:
"""
DEPARTMENTS = [
    ['Dermatology', 'Dermatology is the branch of medicine dealing with the skin, nails, hair and its diseases. It is a specialty with both medical and surgical aspects. A dermatologist treats diseases, in the widest sense, and some cosmetic problems of the skin, scalp, hair, and nails.'],
    ['Cardiology', 'Cardiology, or cardiovascular medicine, is a clinical department set up by the Department of Internal Medicine at all levels of hospitals for the treatment of cardiovascular diseases, including angina pectoris, hypertension, sudden death, arrhythmia, heart failure, premature beats, arrhythmia, myocardial infarction, cardiomyopathy, myocarditis, acute myocardial infarction, and other cardiovascular diseases.'],
    ['Pediatrics', 'Pediatrics is the branch of medicine that involves the medical care of infants, children, and adolescents. The American Academy of Pediatrics recommends people be under pediatric care up to the age of 21.'],
    ['Gynecology', 'Gynecology is a subspecialty of obstetrics and gynecology, and is a specialized department that focuses on the treatment of female gynecological diseases, divided into Western gynecology and Chinese gynecology. Diseases of the female reproductive system are gynecological diseases, including vulvar diseases, vaginal diseases, uterine diseases, etc. can be treated by the pre-external method. There are many types of gynecological diseases, the common ones are: uterine fibroids, ovarian cysts, vaginitis, cervicitis, cervical erosion, pelvic inflammatory disease, adnexitis, functional uterine bleeding, breast disease, infertility, irregular menstruation, endometritis, abnormal leucorrhea and so on. Women should know some basic medical knowledge about menstruation, fertility, pregnancy, childbirth, menopause, etc. from their youth, and often maintain an optimistic mood so that they can avoid or reduce the occurrence of certain obstetrical and gynecological diseases.' ],
    ['Obstetrics and Gynecology', 'Obstetrics and gynecology is one of the four main disciplines of clinical medicine, which focuses on the etiology, pathology, diagnosis and prevention of female reproductive organ diseases, physiological and pathological changes in pregnancy and childbirth, prevention and treatment of high-risk pregnancy and obstructed labor, female reproductive endocrinology, family planning and women\'s health care.'],
    ['Gastroenterology', 'Gastroenterology is the branch of medicine focused on the digestive system and its disorders. Physicians practicing in this field are called gastroenterologists. Gastroenterology is a specialty with both medical and surgical aspects. Physicians practicing in this field are called gastroenterologists.'],
    ['Urology', 'Urology is a medical discipline that specializes in the study of the male and female urinary tracts and the male reproductive system, which is largely subdivided from surgery. In men, the urinary and reproductive systems are inextricably linked, while in women, the urinary tract opens at the vulva.'],
    ['Orthopedics', 'Orthopedics is the branch of surgery concerned with conditions involving the musculoskeletal system. Orthopedic surgeons use both surgical and nonsurgical means to treat musculoskeletal trauma, spine diseases, sports injuries, degenerative diseases, infections, tumors, and congenital disorders.'],
    ['Respiratory Medicine', 'Respiratory medicine is a branch of medicine that deals with diseases of the respiratory tract. Physicians who specialize in this area are called pulmonologists, while those who specialize in surgery are called thoracic surgeons.'],
    ['General Medicine', 'General medicine is a branch of medicine that deals with the diagnosis and treatment of diseases that are not limited to a particular organ system. It is a specialty with both medical and surgical aspects.'],
    ['Endocrinology', 'Endocrinology is a branch of medicine that deals with the endocrine system, its diseases, and its specific secretions known as hormones. Endocrinology is a specialty with both medical and surgical aspects.'],
    ['Cardiology', 'Cardiology, or cardiovascular medicine, is a clinical department set up by the Department of Internal Medicine at all levels of hospitals for the treatment of cardiovascular diseases, including angina pectoris, hypertension, sudden death, arrhythmia, heart failure, premature beats, arrhythmia, myocardial infarction, cardiomyopathy, myocarditis, acute myocardial infarction, and other cardiovascular diseases.'],
    ['Neurology', 'Neurology is a branch of medicine dealing with disorders of the nervous system. Neurological practice relies heavily on the field of neuroscience, the scientific study of the nervous system. Neurologists are medically qualified to practice medicine, and are trained to investigate, or diagnose and treat neurological disorders.'],
    ['Nephrology', 'Nephrology is a branch of medicine and pediatrics that concerns itself with the kidneys: the study of normal kidney function and kidney problems, the preservation of kidney health, and the treatment of kidney diseases, from diet and medication to renal replacement therapy.'],
    ['General Surgery', 'General surgery is a surgical specialty that focuses on abdominal contents including esophagus, stomach, small intestine, colon, liver, pancreas, gallbladder, bile ducts and often the thyroid gland. In addition, the surgeon may treat diseases involving the skin, breast, soft tissue, endocrine system, vascular system, lymphatic system, and hernias.'],
    ['Neurosurgery', 'Neurosurgery is the medical specialty concerned with the prevention, diagnosis, treatment, and rehabilitation of disorders which affect any portion of the nervous system including the brain, spinal cord, peripheral nerves, and extra-cranial cerebrovascular system, and its supportive structures.'],
    ['Cardio-Thoracic Surgery', 'Cardio-thoracic surgery is a surgical specialty that deals with the diagnosis and surgical treatment of diseases of the heart, lungs, esophagus, chest wall, diaphragm, and great vessels.'],
    ['Hepatobiliary pancreatic surgery', 'Hepatobiliary pancreatic surgery is a surgical specialty that deals with the diagnosis and surgical treatment of diseases of the liver, gallbladder, bile ducts, pancreas, and spleen.'],
    ['Ophthalmology', 'Ophthalmology is the branch of medicine that deals with the anatomy, physiology and diseases of the eyeball and orbit. An ophthalmologist is a specialist in medical and surgical eye problems. The field of ophthalmology can be broken down into three main areas: medical ophthalmology, surgical ophthalmology, and vision science.'],
    ['Otolaryngology', 'Otolaryngology is a surgical subspecialty within medicine that deals with conditions of the ear, nose, and throat and related structures of the head and neck. Otolaryngologists are medically qualified to practice medicine, and are trained to investigate, or diagnose and treat ear, nose, and throat disorders.'],
    ['Psychiatry', 'Psychiatry is the medical specialty devoted to the diagnosis, prevention, study, and treatment of mental disorders. These include various abnormalities related to mood, behaviour, cognition, and perceptions. Psychiatrists are medical doctors who specialize in the diagnosis and treatment of mental illness.'],
    ['Oncology', 'Oncology is a branch of medicine that deals with cancer. The role of the oncologist is to manage cancer patients as a team with other specialists. This may include medical oncologists, radiation oncologists, surgical oncologists, gynecologic oncologists, pediatric oncologists, and others.'],
    ['Radiology', 'Radiology is a medical specialty that uses medical imaging to diagnose and treat diseases seen within the body. Radiologists use an imaging technique called radiography to view the interior of a patient\'s body. Radiology is a medical specialty that uses medical imaging to diagnose and treat diseases seen within the body. Radiologists use an imaging technique called radiography to view the interior of a patient\'s body.'],
    ['Internal Medicine', 'Internal medicine is the medical specialty dealing with the prevention, diagnosis, and treatment of adult diseases. Physicians specializing in internal medicine are called internists, or physicians (without a modifier). Internists are skilled in the management of patients who have undifferentiated or multi-system disease processes.'],
    ['Physical Medicine and Rehabilitation', 'Physical medicine and rehabilitation (PM&R), also known as physiatry, is a branch of medicine concerned with the diagnosis and treatment of physical impairments and disabilities. It is a medical specialty that focuses on the diagnosis and treatment of physical impairments and disabilities.'],
    ['Psychology', 'Psychology is the science of behavior and mind, including conscious and unconscious phenomena, as well as feeling and thought. It is an academic discipline of immense scope and diverse interests that, when taken together, seek an understanding of the emergent properties of brains, and all the variety of epiphenomena they manifest. As a social science it aims to understand individuals and groups by establishing general principles and researching specific cases.'],
    ['Thoracic Surgery', 'Thoracic surgery is a surgical subspecialty that focuses on diseases of the chest. Thoracic surgeons are physicians who specialize in diseases of the chest.'],
]

HOSPITAL_LIST = [
    ['Beijing Chaoyang Hospital of Capital Medical University', 'Level III A'],
    ['Xiangya Hospital Central South University', 'Level III A'],
    ['Beijing Tiantan Hospital', 'Level III A'],
    ['The Second Affiliated Hospital Zhejiang University School of Medicine', 'Level III A'],
    ['Tianjin Medical University General Hospital', 'Level III A'],
    ['ChangHai Hospital', 'Level III A'],
    ['West China Hospital Sichuan University', 'Level III A'],
    ['Beijing Xiehe Hospital', 'Level III A'],
    ]

DOCTOR_POSITION = [
    'Director Physician',
    'Assistant Director Physician'
    'Attending Physician'
]
