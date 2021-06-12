from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from . forms import PitchForm, CommentForm, CategoryForm
from .import main
from .. import db
from ..models import User, Pitch, Comments, PitchCategory, Votes


@main.route('/')
def index():
    '''
    Index pge that displays different pitch categories
    '''
    all_category = PitchCategory.get_categories()
    all_pitches = Pitch.query.order_by('id').all()
    print(all_pitches)

    title = 'pitch-it'
    return render_template('index.html', title = title, categories=all_category, all_pitches=all_pitches)



# @main.route('/category/new-pitch/<int:id>', methods=['GET', 'POST'])

@main.route('/pitch/newpitch',methods= ['POST','GET'])
@login_required
def new_pitch():
    """
    Function that adds a pitch 
    """
    
    pitch = PitchForm()
    if pitch.validate_on_submit():
        title = pitch.pitch_title.data
        category = pitch.pitch_category.data
        yourPitch = pitch.pitch_comment.data

        #update pitch instance

        newPitch = Pitch(pitch_title = title,pitch_category = category,pitch_comment = yourPitch,user= current_user)

        #save pitch
        newPitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'NEW PITCH'
    return render_template('new_pitch.html',title = title,pitchform = pitch)  

@main.route('/categories/<int:id>')
def category(id):
    category = PitchCategory.query.get(id)
    if category is None:
        abort(404)

    pitches=Pitch.get_pitches(id)
    return render_template('category.html', pitches=pitches, category=category)


@main.route('/add/category', methods=['GET','POST'])
@login_required
def new_category():
    """
    View new group route function that returns a page with a form to create a category
    """
    
    form = CategoryForm()

    if form.validate_on_submit():
        name = form.name.data
        new_category = PitchCategory(name = name)
        new_category.save_category()

        return redirect(url_for('.index'))

    title = 'New category'
    return render_template('new_category.html', category_form = form, title = title)



@main.route('/view-pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def view_pitch(id):
 
    all_category = PitchCategory.get_categories()
    pitches = Pitch.query.get(id)
    

    if pitches is None:
        abort(404)
    
    comment = Comments.get_comments(id)
    count_likes = Votes.query.filter_by(pitches_id=id, vote=1).all()
    count_dislikes = Votes.query.filter_by(pitches_id=id, vote=2).all()
    return render_template('view-pitch.html', pitches = pitches, comment = comment, count_likes=len(count_likes), count_dislikes=len(count_dislikes), category_id = id, categories=all_category)


@main.route('/write_comment/<int:id>', methods=['GET', 'POST'])
# @login_required
# def post_comment(id):
#     """ 
#     Function to post comments 
#     """
    
#     form = CommentForm()
#     title = 'post comment'
#     pitches = Pitch.query.filter_by(id=id).first()

#     if pitches is None:
#          abort(404)

#     if form.validate_on_submit():
#         opinion = form.opinion.data
#         new_comment = Comments(opinion = opinion, user_id = current_user.id, pitches_id = pitches.id)
#         new_comment.save_comment()
#         return redirect(url_for('.view_pitch', id = pitches.id))

#     return render_template('comments.html', comment_form = form, title = title)
@main.route('/comment/<int:id>',methods= ['POST','GET'])
@login_required
def viewPitch(id):
    onepitch = Pitch.getPitchId(id)
    comments = Comments.get_comments(id)

    if request.args.get("like"):
        onepitch.likes = onepitch.likes + 1

        db.session.add(onepitch)
        db.session.commit()

        return redirect("/comment/{pitch_id}".format(pitch_id=pitch.id))

    elif request.args.get("dislike"):
        onepitch.dislikes = onepitch.dislikes + 1

        db.session.add(onepitch)
        db.session.commit()

        return redirect("/comment/{pitch_id}".format(pitch_id=pitch.id))

    commentForm = CommentForm()
    if commentForm.validate_on_submit():
        comment = commentForm.text.data

        newComment = Comments(opinion = comment,user = current_user,pitches_id= id)

        newComment.save_comment()

    return render_template('comments.html',commentForm = commentForm,comments = comments,pitch = onepitch)

    








@main.route('/pitch/upvote/<int:id>&<int:vote_type>')
@login_required
def upvote(id,vote_type):
    """
    View function that adds one to the vote_number column in the votes table
    """
 
    votes = Votes.query.filter_by(user_id=current_user.id).all()
    print(f'The new vote is {votes}')
    to_str=f'{vote_type}:{current_user.id}:{id}'
    print(f'The current vote is {to_str}')

    if not votes:
        new_vote = Votes(vote=vote_type, user_id=current_user.id, pitches_id=id)
        new_vote.save_vote()
        # print(len(count_likes))
        print('YOU HAVE new VOTED')

    for vote in votes:
        if f'{vote}' == to_str:
            print('YOU CANNOT VOTE MORE THAN ONCE')
            break
        else:   
            new_vote = Votes(vote=vote_type, user_id=current_user.id, pitches_id=id)
            new_vote.save_vote()
            print('YOU HAVE VOTED')
            break
    
    return redirect(url_for('.view_pitch', id=id))

@main.route('/category/interview',methods= ['GET'])
def displayInterviewCategory():
    interviewPitches = Pitch.get_pitches('interview')
    return render_template('interviewPitches.html',interviewPitches = interviewPitches)
    
@main.route('/category/product',methods= ['POST','GET'])
def displayProductCategory():
    productPitches = Pitch.get_pitches('product')
    return render_template('productPitches.html',productPitches = productPitches)

@main.route('/category/promotion',methods= ['POST','GET'])
def displayPromotionCategory():
    promotionPitches = Pitch.get_pitches('promotion')
    return render_template('promotionPitches.html',promotionPitches = promotionPitches)

@main.route('/category/pickup',methods= ['POST','GET'])
def displayPickupCategory():
    pickuplinePitches = Pitch.get_pitches('pickup')
    return render_template('pickuplinePitches.html',pickuplinePitches = pickuplinePitches)    

