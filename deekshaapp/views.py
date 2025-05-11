from django.shortcuts import render,redirect
from django.contrib import messages
from deekshaapp.models import Assessment,Question,AssessmentResults,Profile,AdvisorSupportTask,Certifications
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,"index.html")

def dairyrecords(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/auth/signin/') 
    data=AdvisorSupportTask.objects.filter(email=request.user)
    context={"data":data}
    return render(request,"dairy.html",context)

def submittask(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/auth/signin/') 
    data=AdvisorSupportTask.objects.filter(email=request.user)
    context={"data":data}
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        taskName=request.POST.get('taskname','')
        scoregrade=request.POST.get('scoregrade','')
        certificate= request.FILES['certificate']
        query=Certifications(email=email,name=name,courseName=taskName,courseScore=scoregrade,courseCertificate=certificate)
        query.save()
        messages.success(request,"Task Submitted Contact Advisor for Approval")
        return redirect('/createprofile/')
    return render(request,"submittask.html",context)


def assessment(request):
    data=Profile.objects.filter(email=request.user)
    if not data:
        messages.warning(request,"Please Create Profile to take assessment")
        return redirect("/createprofile/")
    titlesAssessment=Assessment.objects.all()
    data=Profile.objects.filter(email=request.user) 
    myskills=""
    for i in data:
        myskills=i.skills
    myskills=myskills.strip().split(",")
    print(myskills)
    skills=[]
    for j in myskills:
        r=j.strip().replace(" ", "")
        skills.append(r.upper())
    print(skills)
    titles=Assessment.objects.all()
    skill=[]
    for t in titles:
        skill.append(t.title.upper())
    # print("jobs",jobs)
    # print("resume skills",skills)
    jobmatch=list(set(skill).intersection(set(skills)))
    for i in range(len(jobmatch)):
        jobmatch[i]=jobmatch[i].capitalize()
    
    context={"titles":titles,"jobmatch":jobmatch,"titlesAssessment":titlesAssessment}
    return render(request,"assessment.html",context)


def assessmentquestions(request,str):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/auth/signin/') 


    title=str
    data=Question.objects.filter(assessment__title=title)
    count=[]
    title=""
    for i in data:
        count.append(i.id)
        title=i.assessment
    start=count[0]
    end=count[-1]
    print(title)
    context={"data":data,"start":start,"end":end,"title":title}
    return render(request,"selfassessment.html",context)

def assessmentsubmit(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/auth/signin/') 
    if request.method=="POST":
        start=request.POST.get('start','')
        end=request.POST.get('end','')
        title=request.POST.get('title','')
        start=int(start)
        end=int(end)
        totalscore=(end+1)-start
        gotscore=0
        suggestions=[]
        for i in range(start,end+1):
            a1=request.POST.get(f'option{i}','')
            # print(a1)
            if a1=="notAware":
                data=Question.objects.get(id=i)
                suggestions.append(data.topic)
            answer=Question.objects.get(id=i)
            if answer.answer=='option1':
                answer=answer.option1
            elif(answer.answer=='option2'):
                answer=answer.option2
            elif(answer.answer=='option3'):
                answer=answer.option3
            elif(answer.answer=='option4'):
                answer=answer.option4            

            if answer==a1:
                gotscore=gotscore+1
        # print("Total score",totalscore)   
        # print("Obtained score",gotscore)   
        # print("Course",title)   
        user=request.user
        # print(user)   

#       calculate the score
        percentage=(gotscore/totalscore)*100
        result=""
        if percentage<75:
            result="Fail"
        else:
            result="Pass"
        # save the results
        query=AssessmentResults(user=user,courseTitle=title,obtainedScore=gotscore,score=totalscore,percentageObtained=percentage,result=result,improvementPlans=suggestions)
        query.save()
        print(suggestions)
        messages.success(request,"Assessment Score...")
        return redirect('/pdp/')
    

def pdp(request):
    data=AssessmentResults.objects.filter(user=request.user)
    context={"data":data}
    return render(request,"pdp.html",context)


def Advisorsupport(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/auth/signin/') 
    users=User.objects.filter(is_superuser=True)
    context={"users":users}
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        taskname=request.POST.get('taskname','')
        taskdesc=request.POST.get('taskdesc','')
        taskassignee=request.POST.get('taskassignee','')
        user = User.objects.get(username=taskassignee)
        query=AdvisorSupportTask(name=name,email=email,taskName=taskname,taskDescription=taskdesc,taskAssignedby=user)
        query.save()
        messages.success(request,"Task Assigned")
        return redirect("/dairyrecords/")
    return render(request,"advisorsupport.html",context)


def createprofile(request):
    if not request.user.is_authenticated:        
        messages.warning(request,"Please Login and Try Again")
        return redirect('/auth/signin/')    
    data=Profile.objects.filter(email=request.user)
    if data:
        coursecertificates=Certifications.objects.filter(email=request.user)
        context={"datas":data,"coursecertificates":coursecertificates}
        return render(request,"profile.html",context)
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        alternateNumber = request.POST.get('alternateNumber', '')
        address = request.POST.get('address', '')
        schoolName = request.POST.get('schoolName', '')
        xpercentage = request.POST.get('xpercentage', '')
        xcourse = request.POST.get('xcourse', '')
        xdate = request.POST.get('xdate', '')
        xcity = request.POST.get('xcity', '')
        collegeName = request.POST.get('collegeName', '')
        xiipercentage = request.POST.get('xiipercentage', '')
        xiicourse = request.POST.get('xiicourse', '')
        xiidate = request.POST.get('xiidate', '')
        xiicity = request.POST.get('xiicity', '')
        universityName = request.POST.get('universityName', '')
        universitypercentage = request.POST.get('universitypercentage', '')
        branch = request.POST.get('branch', '')
        startdate = request.POST.get('startdate', '')
        enddate = request.POST.get('enddate', '')
        universitycity = request.POST.get('universitycity', '')
        muniversityName = request.POST.get('muniversityName', '')
        muniversitypercentage = request.POST.get('mpercentage', '')
        mbranch = request.POST.get('mbranch', '')
        mstartdate = request.POST.get('mstartdate', '')
        menddate = request.POST.get('menddate', '')
        muniversitycity = request.POST['muniversitycity']
        skills = request.POST.get('skills', '')
        p1 = request.POST.get('p1', '')
        p1d = request.POST.get('p1d', '')
        p2 = request.POST.get('p2', '')
        p2d = request.POST.get('p2d', '')
        i1 = request.POST.get('i1', '')
        i1d = request.POST.get('i1d', '')
        i2 = request.POST.get('i2', '')
        i2d = request.POST.get('i2d', '')
        github = request.POST.get('github', '')
        linkedin = request.POST.get('linkedin', '')
        facebook = request.POST.get('facebook', '')
        instagram = request.POST.get('instagram', '')
        role = request.POST.get('role', '')
        summary = request.POST.get('summary', '')
        query=Profile(name=name,email=email,phone=phone,alternateNumber=alternateNumber,address=address,schoolName=schoolName,xpercentage=xpercentage,xcourse=xcourse,xdate=xdate,xcity=xcity,collegeName=collegeName,xiipercentage=xiipercentage,xiicourse=xiicourse,xiidate=xiidate,xiicity=xiicity,universityName=universityName,universitypercentage=universitypercentage,branch=branch,startdate=startdate,enddate=enddate,universitycity=universitycity,muniversityName=muniversityName,muniversitypercentage=muniversitypercentage,mbranch=mbranch,mstartdate=mstartdate,menddate=menddate,muniversitycity=muniversitycity,skills=skills,p1=p1,p1d=p1d,p2=p2,p2d=p2d,i1=i1,i1d=i1d,i2=i2,i2d=i2d,github=github,linkedin=linkedin,facebook=facebook,instagram=instagram,role=role,summary=summary)
        query.save()
        messages.success(request,"Profile Created Successfully")
        return redirect('/createprofile')
    return render(request,"createprofile.html")



def updateprofile(request,str):
    email=str
    data=Profile.objects.get(email=email)
    print(data)
    context={"data":data}
    if request.method=="POST":
        try:
            name = request.POST.get('name', '')
            dp = request.FILES['dp']
            phone = request.POST.get('phone', '')
            alternateNumber = request.POST.get('alternateNumber', '')
            address = request.POST.get('address', '')
            schoolName = request.POST.get('schoolName', '')
            xpercentage = request.POST.get('xpercentage', '')
            xcourse = request.POST.get('xcourse', '')
            xdate = request.POST.get('xdate', '')
            xcity = request.POST.get('xcity', '')
            collegeName = request.POST.get('collegeName', '')
            xiipercentage = request.POST.get('xiipercentage', '')
            xiicourse = request.POST.get('xiicourse', '')
            xiidate = request.POST.get('xiidate', '')
            xiicity = request.POST.get('xiicity', '')
            universityName = request.POST.get('universityName', '')
            universitypercentage = request.POST.get('universitypercentage', '')
            branch = request.POST.get('branch', '')
            startdate = request.POST.get('startdate', '')
            enddate = request.POST.get('enddate', '')
            universitycity = request.POST.get('universitycity', '')
            muniversityName = request.POST.get('muniversityName', '')
            muniversitypercentage = request.POST.get('mpercentage', '')
            mbranch = request.POST.get('mbranch', '')
            mstartdate = request.POST.get('mstartdate', '')
            menddate = request.POST.get('menddate', '')
            muniversitycity = request.POST['muniversitycity']
            skills = request.POST.get('skills', '')
            p1 = request.POST.get('p1', '')
            p1d = request.POST.get('p1d', '')
            p1l = request.POST.get('p1l', '')
            p2 = request.POST.get('p2', '')
            p2d = request.POST.get('p2d', '')
            p2l = request.POST.get('p2l', '')
            i1 = request.POST.get('i1', '')
            i1d = request.POST.get('i1d', '')
            i2 = request.POST.get('i2', '')
            i2d = request.POST.get('i2d', '')
            github = request.POST.get('github', '')
            linkedin = request.POST.get('linkedin', '')
            facebook = request.POST.get('facebook', '')
            instagram = request.POST.get('instagram', '')
            role = request.POST.get('role', '')
            summary = request.POST.get('summary', '')
            edit= data=Profile.objects.get(email=email)
            edit.name=name
            edit.profilepic=dp
            edit.email=email
            edit.phone=phone
            edit.alternateNumber=alternateNumber
            edit.address=address
            edit.schoolName=schoolName
            edit.xpercentage=xpercentage
            edit.xcourse=xcourse
            edit.xdate=xdate
            edit.xcity=xcity
            edit.collegeName=collegeName
            edit.xiipercentage=xiipercentage
            edit.xiicourse=xiicourse
            edit.xiidate=xiidate
            edit.xiicity=xiicity
            edit.universityName=universityName
            edit.universitypercentage=universitypercentage
            edit.branch=branch
            edit.startdate=startdate
            edit.enddate=enddate
            edit.universitycity=universitycity
            edit.muniversityName=muniversityName
            edit.muniversitypercentage=muniversitypercentage
            edit.mbranch=mbranch
            edit.mstartdate=mstartdate
            edit.menddate=menddate
            edit.muniversitycity=muniversitycity
            edit.skills=skills
            edit.p1=p1
            edit.p1d=p1d
            edit.p1l=p1l
            edit.p2=p2
            edit.p2d=p2d
            edit.p2l=p2l
            edit.i1=i1
            edit.i1d=i1d
            edit.i2=i2
            edit.i2d=i2d
            edit.github=github
            edit.linkedin=linkedin
            edit.facebook=facebook
            edit.instagram=instagram
            edit.role=role
            edit.summary=summary
            edit.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect('/createprofile')
        except:
            name = request.POST.get('name', '')
            phone = request.POST.get('phone', '')
            alternateNumber = request.POST.get('alternateNumber', '')
            address = request.POST.get('address', '')
            schoolName = request.POST.get('schoolName', '')
            xpercentage = request.POST.get('xpercentage', '')
            xcourse = request.POST.get('xcourse', '')
            xdate = request.POST.get('xdate', '')
            xcity = request.POST.get('xcity', '')
            collegeName = request.POST.get('collegeName', '')
            xiipercentage = request.POST.get('xiipercentage', '')
            xiicourse = request.POST.get('xiicourse', '')
            xiidate = request.POST.get('xiidate', '')
            xiicity = request.POST.get('xiicity', '')
            universityName = request.POST.get('universityName', '')
            universitypercentage = request.POST.get('universitypercentage', '')
            branch = request.POST.get('branch', '')
            startdate = request.POST.get('startdate', '')
            enddate = request.POST.get('enddate', '')
            universitycity = request.POST.get('universitycity', '')
            muniversityName = request.POST.get('muniversityName', '')
            muniversitypercentage = request.POST.get('mpercentage', '')
            mbranch = request.POST.get('mbranch', '')
            mstartdate = request.POST.get('mstartdate', '')
            menddate = request.POST.get('menddate', '')
            muniversitycity = request.POST['muniversitycity']
            skills = request.POST.get('skills', '')
            p1 = request.POST.get('p1', '')
            p1d = request.POST.get('p1d', '')
            p1l = request.POST.get('p1l', '')
            p2 = request.POST.get('p2', '')
            p2d = request.POST.get('p2d', '')
            p2l = request.POST.get('p2l', '')
            i1 = request.POST.get('i1', '')
            i1d = request.POST.get('i1d', '')
            i2 = request.POST.get('i2', '')
            i2d = request.POST.get('i2d', '')
            github = request.POST.get('github', '')
            linkedin = request.POST.get('linkedin', '')
            facebook = request.POST.get('facebook', '')
            instagram = request.POST.get('instagram', '')
            role = request.POST.get('role', '')
            summary = request.POST.get('summary', '')
            edit= data=Profile.objects.get(email=email)
            edit.name=name
            edit.email=email
            edit.phone=phone
            edit.alternateNumber=alternateNumber
            edit.address=address
            edit.schoolName=schoolName
            edit.xpercentage=xpercentage
            edit.xcourse=xcourse
            edit.xdate=xdate
            edit.xcity=xcity
            edit.collegeName=collegeName
            edit.xiipercentage=xiipercentage
            edit.xiicourse=xiicourse
            edit.xiidate=xiidate
            edit.xiicity=xiicity
            edit.universityName=universityName
            edit.universitypercentage=universitypercentage
            edit.branch=branch
            edit.startdate=startdate
            edit.enddate=enddate
            edit.universitycity=universitycity
            edit.muniversityName=muniversityName
            edit.muniversitypercentage=muniversitypercentage
            edit.mbranch=mbranch
            edit.mstartdate=mstartdate
            edit.menddate=menddate
            edit.muniversitycity=muniversitycity
            edit.skills=skills
            edit.p1=p1
            edit.p1d=p1d
            edit.p1l=p1l
            edit.p2=p2
            edit.p2d=p2d
            edit.p2l=p2l
            edit.i1=i1
            edit.i1d=i1d
            edit.i2=i2
            edit.i2d=i2d
            edit.github=github
            edit.linkedin=linkedin
            edit.facebook=facebook
            edit.instagram=instagram
            edit.role=role
            edit.summary=summary
            edit.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect('/createprofile')
    return render(request,"updateprofile.html",context)