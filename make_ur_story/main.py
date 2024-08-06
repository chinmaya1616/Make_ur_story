from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
        <head>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background: linear-gradient(to right, #ff7e5f, #feb47b);
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    overflow: hidden;
                }
                .container {
                    width: 90%;
                    max-width: 700px;
                    padding: 30px;
                    background: #fff;
                    border-radius: 20px;
                    box-shadow: 0 30px 60px rgba(0,0,0,0.3);
                    text-align: center;
                    position: relative;
                    transform-style: preserve-3d;
                    transform: perspective(1500px) rotateX(5deg) rotateY(5deg);
                    transition: transform 0.5s;
                }
                .container:hover {
                    transform: perspective(1500px) rotateX(0deg) rotateY(0deg);
                }
                h1 {
                    color: #333;
                    font-size: 2.5em;
                    margin-bottom: 30px;
                    text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
                    transform: translateZ(20px);
                }
                form {
                    display: flex;
                    flex-direction: column;
                    gap: 15px;
                }
                label {
                    font-weight: bold;
                    color: #444;
                    font-size: 1.2em;
                }
                input[type="text"], select {
                    padding: 12px;
                    border: 2px solid #ddd;
                    border-radius: 12px;
                    box-shadow: inset 0 8px 16px rgba(0,0,0,0.2), 0 8px 16px rgba(0,0,0,0.1);
                    font-size: 1em;
                    transition: all 0.3s ease;
                }
                input[type="text"]:focus, select:focus {
                    border-color: #ff6f61;
                    box-shadow: inset 0 8px 16px rgba(0,0,0,0.2), 0 12px 24px rgba(0,0,0,0.2);
                }
                input[type="submit"] {
                    background: linear-gradient(to right, #ff6f61, #de6262);
                    color: white;
                    border: none;
                    padding: 15px;
                    border-radius: 12px;
                    cursor: pointer;
                    font-size: 1.2em;
                    transition: background 0.3s, transform 0.3s, box-shadow 0.3s;
                    box-shadow: 0 10px 20px rgba(0,0,0,0.3);
                    position: relative;
                }
                input[type="submit"]:hover {
                    background: linear-gradient(to right, #de6262, #ff6f61);
                    transform: scale(1.05);
                    box-shadow: 0 12px 24px rgba(0,0,0,0.4);
                }
                .story {
                    background: #fff;
                    padding: 30px;
                    border-radius: 20px;
                    box-shadow: 0 30px 60px rgba(0,0,0,0.3);
                    margin-top: 30px;
                    text-align: left;
                    color: #333;
                    line-height: 1.8;
                    transform-style: preserve-3d;
                    transform: perspective(1500px) rotateX(5deg) rotateY(-5deg);
                    transition: transform 0.5s;
                }
                .story:hover {
                    transform: perspective(1500px) rotateX(0deg) rotateY(0deg);
                }
                h2 {
                    color: #ff6f61;
                    font-size: 1.8em;
                    margin-top: 0;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                }
                p {
                    margin: 10px 0;
                    padding: 15px;
                    border-radius: 8px;
                    background: #f9f9f9;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                    position: relative;
                    transform: translateZ(10px);
                }
                p::before {
                    content: "";
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background: linear-gradient(135deg, rgba(0,0,0,0.1), rgba(255,255,255,0));
                    border-radius: 8px;
                    z-index: -1;
                    transform: scale(1.1);
                }
                .additional-info {
                    margin-top: 30px;
                    padding: 20px;
                    border-radius: 10px;
                    background: #f9f9f9;
                    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
                }
                .additional-info h3 {
                    color: #ff6f61;
                    margin-bottom: 15px;
                }
                .additional-info textarea {
                    width: 100%;
                    padding: 10px;
                    border: 2px solid #ddd;
                    border-radius: 8px;
                    font-size: 1em;
                    box-shadow: inset 0 4px 8px rgba(0,0,0,0.1);
                }
                .additional-info input[type="submit"] {
                    margin-top: 10px;
                    background: linear-gradient(to right, #ff6f61, #de6262);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Story Generator</h1>
                <form action="/story" method="post">
                    <label for="noun1">Character Name (Boy):</label>
                    <input type="text" id="noun1" name="noun1" required>
                    <label for="noun2">Character Name (Girl):</label>
                    <input type="text" id="noun2" name="noun2" required>
                    <label for="story_type">Select Story Type:</label>
                    <select id="story_type" name="story_type" required>
                        <option value="thriller">Thriller</option>
                        <option value="romance">Romance</option>
                        <option value="action">Action</option>
                        <option value="heartbroken">Heartbroken</option>
                        <option value="funny">Funny</option>
                    </select>
                    <input type="submit" value="Generate Story">
                </form>
            </div>
        </body>
        </html>
    '''

@app.route('/story', methods=['POST'])
def story():
    noun1 = request.form['noun1']
    noun2 = request.form['noun2']
    story_type = request.form['story_type']

    if story_type == 'thriller':
        story = f"""
        <div class='story'>
            <h2>**In the dark city of Shadowvale,**</h2>
            <p>Detective <strong>{noun1}</strong> was known for his unyielding pursuit of justice. His reputation for solving the most perplexing cases was unmatched. But when a series of mysterious disappearances plagued the city, even <strong>{noun1}</strong> was puzzled.</p>
            <p>Rumors swirled around the shadowy figure known only as <strong>{noun2}</strong>, a villain whose cunning and ruthlessness made him a ghost in the city’s underworld. The authorities were desperate, and every clue seemed to lead back to <strong>{noun2}</strong>.</p>
            <p>One rainy night, <strong>{noun1}</strong> received an anonymous tip leading him to an abandoned warehouse. The place was dark, the air thick with the scent of mildew and rust. As he carefully made his way inside, the silence was almost deafening.</p>
            <p>Suddenly, a light flickered on, revealing <strong>{noun2}</strong> sitting calmly in the middle of the room, a menacing grin playing on his lips. "Detective," <strong>{noun2}</strong> said smoothly, "you've been a thorn in my side for far too long."</p>
            <p>"Why are you doing this?" <strong>{noun1}</strong> demanded, his voice steady despite the tension. "What’s your endgame?"</p>
            <p><strong>{noun2}</strong> laughed softly, the sound echoing eerily in the large space. "Power is not my goal," he said. "It’s chaos. I wanted to see if someone like you could actually make a difference, and now, you’re about to prove it—or fail miserably."</p>
            <p>The confrontation escalated quickly, a game of wits and nerve. In the end, <strong>{noun1}</strong> managed to outsmart <strong>{noun2}</p>            <p>The confrontation escalated quickly, a game of wits and nerve. In the end, <strong>{noun1}</strong> managed to outsmart <strong>{noun2}</strong>, using his expertise and a clever trap to capture the elusive villain. As <strong>{noun2}</strong> was led away in handcuffs, the city of Shadowvale breathed a sigh of relief. The darkness had been vanquished, at least for now, thanks to the unyielding resolve of Detective <strong>{noun1}</strong>.</p>
            <h2>**The end.**</h2>
        </div>
        """

    elif story_type == 'romance':
        story = f"""
        <div class='story'>
            <h2>**A Love Blossoms in the City of Lights**</h2>
            <p>In the bustling streets of Paris, two souls were destined to meet. <strong>{noun1}</strong>, a talented artist with dreams as grand as the Eiffel Tower, found solace in painting the city's vibrant landscapes. <strong>{noun2}</strong>, a passionate writer, wandered the same streets in search of inspiration for her next novel.</p>
            <p>One rainy afternoon, their paths crossed in a quaint café tucked away from the city's chaos. <strong>{noun1}</strong> was sketching the view from the window, while <strong>{noun2}</strong> was lost in her thoughts, scribbling away in her notebook.</p>
            <p>Their eyes met, and in that moment, a spark ignited. They began talking, sharing their dreams and passions, and discovering a deep connection. As days turned into weeks, their bond grew stronger, filled with laughter, art, and love.</p>
            <p>One evening, as the sun set behind the city skyline, <strong>{noun1}</strong> took <strong>{noun2}</strong> to the top of Montmartre, where they watched the city lights twinkle below. In that magical moment, <strong>{noun1}</strong> confessed his love, and <strong>{noun2}</strong> felt her heart flutter with joy.</p>
            <p>The city of lights had witnessed the beginning of a beautiful love story, a tale that would continue to shine brightly in their hearts forever.</p>
            <h2>**The end.**</h2>
        </div>
        """

    elif story_type == 'action':
        story = f"""
        <div class='story'>
            <h2>**The Ultimate Rescue Mission**</h2>
            <p>In a world on the brink of chaos, <strong>{noun1}</strong>, a skilled covert operative, was given a critical mission. The notorious villain, <strong>{noun2}</strong>, had taken control of a top-secret military base and was threatening to unleash a devastating weapon.</p>
            <p>With a team of elite agents, <strong>{noun1}</strong> embarked on a daring mission to infiltrate the base. The operation was fraught with danger, with traps and enemies around every corner. But <strong>{noun1}</strong> was prepared, using advanced gadgets and combat skills to outmaneuver <strong>{noun2}</strong>’s henchmen.</p>
            <p>As they reached the control room, <strong>{noun1}</strong> faced <strong>{noun2}</strong> in an intense showdown. The battle was fierce, with explosions and close calls. In the end, <strong>{noun1}</strong> managed to disarm the weapon and capture <strong>{noun2}</strong>, ensuring that the world would be safe once more.</p>
            <p>Victorious but exhausted, <strong>{noun1}</strong> and the team returned to base, knowing that they had averted disaster and saved countless lives. The mission was a success, and the world was a safer place thanks to their bravery and skill.</p>
            <h2>**The end.**</h2>
        </div>
        """

    elif story_type == 'heartbroken':
        story = f"""
        <div class='story'>
            <h2>**A Love Lost and Remembered**</h2>
            <p>In a small, quiet town, <strong>{noun1}</strong> and <strong>{noun2}</strong> had shared a love that was pure and deep. Their time together was filled with joy, dreams, and plans for a future together. However, life had other plans, and circumstances pulled them apart.</p>
            <p>Months passed, and the memories of their time together lingered like shadows in <strong>{noun1}</strong>’s heart. Every corner of the town held echoes of their laughter, every sunset a reminder of their shared dreams. The absence of <strong>{noun2}</strong> was a constant ache, a reminder of what once was.</p>
            <p>One day, while walking through a park they used to visit, <strong>{noun1}</strong> came across an old photograph of them together, tucked away in a book. The image brought back a flood of memories and emotions, a bittersweet reminder of their time together.</p>
            <p>With a heavy heart, <strong>{noun1}</strong> sat by their favorite spot, reflecting on the love they had lost. Although the pain was sharp, it was also accompanied by a deep sense of gratitude for having experienced such a profound connection. The memories of <strong>{noun2}</strong> would forever remain in <strong>{noun1}</strong>’s heart, a testament to a love that was beautiful while it lasted.</p>
            <h2>**The end.**</h2>
        </div>
        """
    elif story_type == 'funny':
        story = f"""
           <div class='story'>
               <h2>**The Great Pie Incident**</h2>
               <p>In the quirky town of Quirkville, everyone knew that the annual pie-baking contest was the highlight of the year. <strong>{noun1}</strong> and <strong>{noun2}</strong> were the most competitive bakers, each determined to win the coveted Golden Rolling Pin trophy.</p>
               <p>This year, <strong>{noun1}</strong> decided to experiment with a "mystery ingredient," which turned out to be a secret blend of exotic spices. Meanwhile, <strong>{noun2}</strong> opted for a traditional recipe but added a special twist—squirrels were known to love the special nuts she used.</p>
               <p>As the contest kicked off, chaos erupted. <strong>{noun1}</strong>’s pie began to emit a cloud of colorful smoke, causing everyone to sneeze and cough. <strong>{noun2}</strong>’s pie, on the other hand, attracted a gang of mischievous squirrels that created pandemonium in the judging area.</p>
               <p>The judges, trying to stay composed, tasted <strong>{noun1}</strong>’s pie while desperately fanning the smoke away. Their faces contorted in confusion and mild panic as the strange flavors danced on their tongues. Then, they turned to <strong>{noun2}</strong>’s pie, which was now surrounded by a small army of squirrels, each trying to steal a piece.</p>
               <p>In the end, the contest was declared a draw. <strong>{noun1}</strong> and <strong>{noun2}</strong> were both awarded honorary titles: <strong>{noun1}</strong> for “Most Mysterious Flavor” and <strong>{noun2}</strong> for “Squirrel’s Choice.” The townspeople laughed heartily, and the incident became the stuff of legend in Quirkville.</p>
               <p>From then on, the annual pie-baking contest was known as the "Great Pie Incident," a humorous reminder that sometimes, the best stories come from the most unexpected and hilarious mishaps.</p>
               <h2>**The end.**</h2>
           </div>
           """
    else:
        story = "<div class='story'><h2>**Unknown Story Type**</h2><p>Sorry, the story type you selected is not available.</p></div>"

    return render_template_string(story)

if __name__ == '__main__':
    app.run(debug=True)