from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text for demonstration
text = {'Learning To Rank': 1}

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(text, max_font_size=200)
file_loc = "C:/Users/ariha/Downloads/GitHub Pages/MLBible.github.io/images/banners/ltr.png"
wordcloud.to_file(file_loc)
