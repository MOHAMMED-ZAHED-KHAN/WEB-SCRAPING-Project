
<h1 align="center">AmbitionBox Company Data Web Scraping Project</h1>

<p align="center">
  A Python-based web scraping project to collect company ratings, reviews, salary information, interview details, and job information from AmbitionBox.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/BeautifulSoup-green" alt="Beautiful Soup">
  <img src="https://img.shields.io/badge/Pandas-purple?logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Companies-820-orange" alt="820 Companies">
  <img src="https://img.shields.io/badge/Output-CSV-yellow" alt="CSV Output">
</p>

---

<h2>📌 Project Overview</h2>

<p>
  This project is a Python-based web scraping application developed to extract company-related information from
  <a href="https://www.ambitionbox.com/">AmbitionBox</a>, a platform that provides insights into companies, workplace ratings, employee reviews, salaries, interview experiences, and job opportunities.
</p>

<p>
  The primary objective of this project is to automate the collection of company information from multiple pages of AmbitionBox company listings. Instead of manually visiting individual pages and collecting information, the scraper uses Python libraries to retrieve webpage content, parse HTML elements, and extract relevant data.
</p>

<p>
  The scraper processes company listing pages and collects six key attributes: company name, rating, reviews, salary information, interview information, and job information. The extracted records are combined into a structured Pandas DataFrame.
</p>

<p>
  <strong>As a result, data for 820 companies was collected and exported to a CSV file.</strong> The resulting dataset can be used for company comparisons, career research, exploratory data analysis, and other data-driven applications.
</p>

<h2>🎯 Project Objectives</h2>

<ul>
  <li>Automate company data collection from AmbitionBox.</li>
  <li>Collect information for 820 companies.</li>
  <li>Extract relevant company details from HTML content.</li>
  <li>Organize the extracted information into a structured tabular format.</li>
  <li>Combine records collected from multiple listing pages into a single dataset.</li>
  <li>Export the final dataset to a CSV file for easy access and reuse.</li>
  <li>Gain practical experience in Python programming, web scraping, and data handling.</li>
</ul>

<h2>📈 Project Statistics</h2>

<table>
  <thead>
    <tr>
      <th>Metric</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data Source</td>
      <td>AmbitionBox</td>
    </tr>
    <tr>
      <td>Companies Collected</td>
      <td>820</td>
    </tr>
    <tr>
      <td>Data Fields</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Programming Language</td>
      <td>Python</td>
    </tr>
    <tr>
      <td>Data Processing</td>
      <td>Pandas</td>
    </tr>
    <tr>
      <td>Output Format</td>
      <td>CSV</td>
    </tr>
  </tbody>
</table>

<h2>📊 Data Fields Extracted</h2>

<p>
  The project collects six types of company-related information from AmbitionBox company listing cards.
</p>

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
      <td>Salary-related information displayed through the company's salary link.</td>
    </tr>
    <tr>
      <td><code>interview</code></td>
      <td>Interview-related information displayed through the company's interview link.</td>
    </tr>
    <tr>
      <td><code>job</code></td>
      <td>Job-related information displayed through the company's job link.</td>
    </tr>
  </tbody>
</table>

<p>
  The availability of individual fields depends on the information displayed on each company card. If a matching HTML element is missing, the scraper stores <code>None</code> for that field.
</p>

<h2>🛠️ Technologies and Libraries Used</h2>

<ul>
  <li>
    <strong>Python:</strong> The core programming language used to implement the scraping workflow.
  </li>
  <li>
    <strong>Requests:</strong> Sends HTTP GET requests to retrieve webpage content.
  </li>
  <li>
    <strong>Beautiful Soup:</strong> Parses HTML documents and extracts relevant company information.
  </li>
  <li>
    <strong>lxml:</strong> HTML parser used with Beautiful Soup to process webpage content.
  </li>
  <li>
    <strong>Pandas:</strong> Creates DataFrames, combines records from multiple pages, inspects the dataset, and exports the collected data to CSV.
  </li>
  <li>
    <strong>CSV:</strong> Stores the collected information in a structured, reusable file format.
  </li>
</ul>

<h2>⚙️ Project Workflow</h2>

<h3>1. Access AmbitionBox Company Listings</h3>

<p>
  The scraper iterates through page numbers from 1 to 100 using a Python <code>for</code> loop. For each page, it constructs the corresponding AmbitionBox URL and sends an HTTP GET request with a User-Agent header.
</p>

<h3>2. Retrieve and Parse Webpage Content</h3>

<p>
  The returned HTML content is parsed using Beautiful Soup with the <code>lxml</code> parser. The code searches for <code>div</code> elements containing the <code>data-testid</code> attribute.
</p>

<h3>3. Identify Company Cards</h3>

<p>
  The scraper filters the matching elements using the <code>loc-company-card-</code> prefix in their <code>data-testid</code> values. These elements represent the company cards from which the required information is extracted.
</p>

<h3>4. Extract Company Information</h3>

<p>
  For each identified company card, the scraper locates the relevant HTML elements and links to extract the six required fields.
</p>

<ul>
  <li>Company names from heading elements.</li>
  <li>Company ratings from the matching rating element.</li>
  <li>Review information from links containing <code>/reviews/</code>.</li>
  <li>Salary information from links containing <code>/salaries/</code>.</li>
  <li>Interview information from links containing <code>/interviews/</code>.</li>
  <li>Job information from links containing <code>/jobs/</code>.</li>
</ul>

<p>
  Conditional checks help the scraper handle missing HTML elements without immediately raising an attribute error.
</p>

<h3>5. Organize the Extracted Data</h3>

<p>
  The extracted values are stored in Python lists and combined into a dictionary. Pandas converts the dictionary into a DataFrame for each page, providing a structured representation of the collected information.
</p>

<h3>6. Combine Records from Multiple Pages</h3>

<p>
  The DataFrames created for individual pages are combined into one final DataFrame using <code>pd.concat()</code> with <code>ignore_index=True</code>. This consolidates the collected records into a single dataset.
</p>

<h3>7. Inspect and Export the Dataset</h3>

<p>
  The final DataFrame is displayed using <code>print(final_df)</code>, and its dimensions are checked using <code>print(final_df.shape)</code>.
</p>

<p>
  Finally, the dataset is exported to a CSV file named <code>WebScarpedJobsData.csv</code>. The resulting file contains the extracted information for 820 companies and can be used independently of the scraping script.
</p>

<h2>📁 Project Output</h2>

<p>
  The main output of this project is a CSV file containing the scraped company information.
</p>

<ul>
  <li><strong>Output file:</strong> <code>WebScrapedCompaniesData.csv</code></li>
  <li><strong>Companies collected:</strong> 820</li>
  <li><strong>Data fields:</strong> 6</li>
  <li><strong>File format:</strong> CSV (Comma-Separated Values)</li>
</ul>

<p>The dataset includes:</p>

<ul>
  <li>Company names</li>
  <li>Company ratings</li>
  <li>Review-related information</li>
  <li>Salary-related information</li>
  <li>Interview-related information</li>
  <li>Job-related information</li>
</ul>

<p>
  The generated CSV file can be opened using Microsoft Excel, Google Sheets, or Python. It provides a reusable dataset for further data cleaning, analysis, and visualization.
</p>

<h2>💻 Installation and Setup</h2>

<h3>Prerequisites</h3>

<p>
  Install Python on your system and install the required libraries using pip:
</p>

<pre><code>pip install pandas requests beautifulsoup4 lxml</code></pre>

<h3>How to Run the Project</h3>

<ol>
  <li>Clone or download the repository from GitHub.</li>
  <li>Open the project folder in your preferred code editor.</li>
  <li>Ensure that all required Python libraries are installed.</li>
  <li>Execute the Python scraping script.</li>
  <li>Allow the script to process the company listing pages.</li>
  <li>After successful execution, the extracted records will be combined and exported to the CSV file.</li>
</ol>

<p>Run the script from your terminal:</p>

<pre><code>python ScrapingDataFromAmbitionBoxWebsite.py</code></pre>

<p>
  The CSV file will be saved in the current working directory unless another output path is specified.
</p>

<h2>🚀 Applications of the Collected Dataset</h2>

<ul>
  <li>
    <strong>Company Comparison:</strong> Compare company ratings and other available company information.
  </li>
  <li>
    <strong>Career Research:</strong> Organize company details while researching potential employers.
  </li>
  <li>
    <strong>Salary Exploration:</strong> Explore salary-related information displayed on company listing cards.
  </li>
  <li>
    <strong>Interview Preparation:</strong> Identify companies with interview-related information for further research.
  </li>
  <li>
    <strong>Job Market Research:</strong> Explore job-related information displayed on company cards.
  </li>
  <li>
    <strong>Exploratory Data Analysis:</strong> Investigate rating distributions, missing values, and patterns in the collected dataset.
  </li>
  <li>
    <strong>Data Visualization:</strong> Create charts and graphs to summarize the available company information.
  </li>
</ul>

<p>
  These are potential applications and future extensions of the collected dataset. Advanced analytics, predictive modeling, and visualizations are not included in the current implementation unless developed separately.
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
  <li>Identify and remove duplicate company records where appropriate.</li>
  <li>Clean the extracted data and convert suitable columns to numeric data types.</li>
  <li>Save the CSV without an additional index column.</li>
  <li>Perform exploratory data analysis using Pandas, Matplotlib, and Seaborn.</li>
  <li>Create visualizations comparing company ratings and available salary information.</li>
  <li>Add logging and progress tracking.</li>
  <li>Adapt the scraper to changes in the website's HTML structure.</li>
  <li>Develop an interactive dashboard to explore the collected company information.</li>
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
