
<h1 align="center">AmbitionBox Company Data Web Scraping Project</h1>

<p align="center">
  A Python-based web scraping project to collect company ratings, reviews, salary information, interview details, and job information from AmbitionBox and export the extracted data to a CSV file.
</p>

---

<h2>📌 Project Overview</h2>

<p>
  This project is a Python-based web scraping application developed to extract company-related information from
  <a href="https://www.ambitionbox.com/">AmbitionBox</a>, a platform that provides insights into companies, workplace ratings, employee reviews, salaries, interview experiences, and job opportunities.
</p>

<p>
  The main objective of this project is to automate the collection of company information from multiple pages of AmbitionBox company listings. Instead of manually visiting each page and collecting information, the scraper uses Python libraries to retrieve webpage content, parse HTML elements, and extract relevant data.
</p>

<p>
  The scraper processes up to 100 company listing pages and extracts six key attributes: company name, rating, reviews, salary information, interview information, and job information. The collected records are combined into a structured Pandas DataFrame and exported to a CSV file for future use.
</p>

<h2>🎯 Project Objectives</h2>

<ul>
  <li>Automate the collection of company information from AmbitionBox.</li>
  <li>Scrape data from up to 100 company listing pages.</li>
  <li>Extract relevant company details from HTML content.</li>
  <li>Organize the extracted information into a structured tabular format.</li>
  <li>Combine records collected from multiple pages into a single dataset.</li>
  <li>Export the final dataset to a CSV file for easy access and reuse.</li>
  <li>Gain practical experience in Python programming, web scraping, and data handling.</li>
</ul>

<h2>📊 Data Fields Extracted</h2>

<p>The project collects the following information from AmbitionBox company listing cards:</p>

<table>
  <thead>
    <tr>
      <th>Column Name</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td>Name of the company.</td>
    </tr>
    <tr>
      <td><code>rating</code></td>
      <td>Company rating displayed on the listing card.</td>
    </tr>
    <tr>
      <td><code>reviews</code></td>
      <td>Review-related information displayed through the company's review link.</td>
    </tr>
    <tr>
      <td><code>sal</code></td>
      <td>Salary-related information displayed on the company's salary link.</td>
    </tr>
    <tr>
      <td><code>interview</code></td>
      <td>Interview-related information displayed on the company's interview link.</td>
    </tr>
    <tr>
      <td><code>job</code></td>
      <td>Job-related information displayed on the company's job link.</td>
    </tr>
  </tbody>
</table>

<p>
  The availability of individual fields depends on the information displayed on each company card. Missing HTML elements are handled by storing <code>None</code> for the corresponding value.
</p>

<h2>🛠️ Technologies and Libraries Used</h2>

<ul>
  <li><strong>Python:</strong> Core programming language used to implement the scraping workflow.</li>
  <li><strong>Requests:</strong> Sends HTTP GET requests to retrieve webpage content.</li>
  <li><strong>Beautiful Soup:</strong> Parses HTML documents and extracts relevant information.</li>
  <li><strong>lxml:</strong> HTML parser used with Beautiful Soup to process webpage content.</li>
  <li><strong>Pandas:</strong> Creates DataFrames, combines records from multiple pages, inspects the dataset, and exports it to CSV.</li>
  <li><strong>CSV:</strong> Output format used to store the collected company information in a structured, reusable file.</li>
</ul>

<h2>⚙️ Project Workflow</h2>

<h3>1. Access AmbitionBox Company Listings</h3>

<p>
  The scraper iterates through page numbers from 1 to 100 using a Python <code>for</code> loop. For each page, it constructs the corresponding URL and sends an HTTP GET request with a User-Agent header.
</p>

<h3>2. Retrieve and Parse Webpage Content</h3>

<p>
  The returned HTML content is parsed using Beautiful Soup with the <code>lxml</code> parser. The code searches for <code>div</code> elements containing a <code>data-testid</code> attribute.
</p>

<h3>3. Identify Company Cards</h3>

<p>
  The scraper filters matching elements using the <code>loc-company-card-</code> prefix in their <code>data-testid</code> values. These elements represent the company cards from which information is extracted.
</p>

<h3>4. Extract Company Information</h3>

<p>For each identified company card, the scraper locates the relevant HTML elements and links to extract:</p>

<ul>
  <li>Company names from heading elements.</li>
  <li>Company ratings from the matching rating element.</li>
  <li>Review information from links containing <code>/reviews/</code>.</li>
  <li>Salary information from links containing <code>/salaries/</code>.</li>
  <li>Interview information from links containing <code>/interviews/</code>.</li>
  <li>Job information from links containing <code>/jobs/</code>.</li>
</ul>

<p>
  Conditional checks help the scraper handle missing elements without immediately raising an attribute error when a field is unavailable.
</p>

<h3>5. Organize the Extracted Data</h3>

<p>
  The extracted values are stored in Python lists and combined into a dictionary. Pandas converts this dictionary into a DataFrame for each page.
</p>

<h3>6. Combine Data from Multiple Pages</h3>

<p>
  The DataFrames created for individual pages are combined into a single final DataFrame using <code>pd.concat()</code> with <code>ignore_index=True</code>.
</p>

<h3>7. Inspect and Export the Final Dataset</h3>

<p>
  The code displays the final DataFrame and its dimensions using <code>print(final_df)</code> and <code>print(final_df.shape)</code>.
</p>

<p>
  Finally, the collected records are exported to a CSV file named <code>WebScarpedJobsData.csv</code>. The resulting dataset can be used independently of the scraping script for further processing and analysis.
</p>

<h2>📁 Project Output</h2>

<p>The main output of this project is a CSV file containing the scraped company data.</p>

<ul>
  <li><strong>Output file:</strong> <code>WebScarpedJobsData.csv</code></li>
  <li><strong>Format:</strong> CSV (Comma-Separated Values)</li>
  <li><strong>Data organization:</strong> Six columns containing company-related information.</li>
</ul>

<p>The CSV file contains:</p>

<ul>
  <li>Company name</li>
  <li>Company rating</li>
  <li>Review information</li>
  <li>Salary information</li>
  <li>Interview information</li>
  <li>Job information</li>
</ul>

<p>
  The dataset can be opened using Microsoft Excel, Google Sheets, or Python. It also provides a foundation for future data cleaning, exploratory data analysis, and visualization.
</p>

<h2>💻 Installation and Setup</h2>

<h3>Prerequisites</h3>

<p>Install Python on your system and install the required libraries:</p>

<pre><code>pip install pandas requests beautifulsoup4 lxml</code></pre>

<h3>How to Run the Project</h3>

<ol>
  <li>Clone or download the repository from GitHub.</li>
  <li>Open the project folder in your preferred code editor.</li>
  <li>Ensure that all required Python libraries are installed.</li>
  <li>Run the Python scraping script.</li>
  <li>Allow the script to process the listing pages.</li>
  <li>After successful execution, the extracted records will be combined and exported to the CSV file.</li>
</ol>

<p>Run the script from your terminal:</p>

<pre><code>python ScrapingDataFromAmbitionBoxWebsite.py</code></pre>

<p>
  The output CSV file will be saved in the current working directory unless another path is specified.
</p>

<h2>🚀 Applications of the Collected Dataset</h2>

<ul>
  <li><strong>Company Comparison:</strong> Compare company ratings and other available information.</li>
  <li><strong>Career Research:</strong> Organize company details while researching potential employers.</li>
  <li><strong>Salary Exploration:</strong> Explore salary-related information available on company listing cards.</li>
  <li><strong>Interview Preparation:</strong> Identify companies with interview-related information for further research.</li>
  <li><strong>Job Market Research:</strong> Explore job-related information displayed on company cards.</li>
  <li><strong>Exploratory Data Analysis:</strong> Investigate rating distributions, missing values, and other patterns in the dataset.</li>
  <li><strong>Data Visualization:</strong> Create charts and graphs to summarize the available company information.</li>
</ul>

<p>
  These are potential applications and future extensions of the dataset. Advanced analytics and visualizations are not included in the current scraping implementation unless developed separately.
</p>

<h2>📚 Key Learnings</h2>

<ul>
  <li>Sending HTTP requests and retrieving webpage content.</li>
  <li>Parsing HTML using Beautiful Soup and lxml.</li>
  <li>Locating HTML elements using tags, attributes, CSS classes, and link patterns.</li>
  <li>Automating data collection across multiple web pages.</li>
  <li>Handling missing HTML elements during extraction.</li>
  <li>Working with Python lists and dictionaries to organize information.</li>
  <li>Creating and combining Pandas DataFrames.</li>
  <li>Exporting structured data to CSV format.</li>
  <li>Understanding practical web scraping challenges, including changing website structures and unavailable fields.</li>
</ul>

<h2>🔮 Future Enhancements</h2>

<ul>
  <li>Add request timeouts, exception handling, and HTTP status checks.</li>
  <li>Improve efficiency by combining page-level records in a single concatenation step.</li>
  <li>Remove duplicate company records where appropriate.</li>
  <li>Clean the extracted data and convert suitable columns to numeric data types.</li>
  <li>Save the CSV without an additional index column.</li>
  <li>Add exploratory data analysis using Pandas, Matplotlib, and Seaborn.</li>
  <li>Develop visualizations to compare company ratings and available salary information.</li>
  <li>Add logging and progress tracking.</li>
  <li>Adapt the scraper to changes in the website's HTML structure.</li>
  <li>Build a dashboard to make the collected company information easier to explore.</li>
</ul>

<h2>⚠️ Disclaimer</h2>

<p>
  This project is intended for educational purposes and demonstrates Python-based web scraping and data collection. Information available on AmbitionBox may change over time. Before running the scraper, review the website's applicable terms of use, robots.txt guidance, access restrictions, and relevant data rights. Use reasonable request rates and do not attempt to bypass access controls.
</p>

<h2>👨‍💻 Author</h2>

<p>
  <strong>Mohammed Zahed Khan</strong>
</p>

<p>
  GitHub Repository:
  <a href="https://github.com/MOHAMMED-ZAHED-KHAN/WEB-SCRAPING-Projects/tree/main/FetchingDataUsingWebScraping">
    WEB-SCRAPING-Projects — FetchingDataUsingWebScraping
  </a>
</p>
