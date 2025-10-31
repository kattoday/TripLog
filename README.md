# 🧳 TripLog — Serverless Travel Logger with Sentiment Filtering

TripLog is a full-stack serverless web app that lets users log trips, analyze their notes using AWS Comprehend, and filter trip history by sentiment. Built with AWS Lambda, API Gateway, DynamoDB, and a lightweight frontend hosted on S3.

---

## 🚀 Features

- ✍️ Submit trips with name, location, date, and notes
- 🧠 Automatic sentiment and entity analysis using AWS Comprehend
- 📦 Store enriched trip data in DynamoDB
- 🔍 Filter trips by sentiment (positive, negative, mixed, neutral)
- 🌐 Frontend hosted on S3, integrated with API Gateway

---

## 🛠️ Tech Stack

| Layer       | Service         |
|------------|------------------|
| Frontend    | HTML/CSS/JS (S3 hosted) |
| API         | AWS API Gateway |
| Backend     | AWS Lambda (Python) |
| NLP         | AWS Comprehend |
| Database    | AWS DynamoDB |

---

## 📁 Folder Structure

```
TripLogWriter/
├── lambda_function.py     # Handles trip submission, Comprehend analysis, DynamoDB write
├── requirements.txt       # Lambda dependencies
└── index.html             # Frontend UI (hosted on S3)
```

---

## 🔧 Setup Instructions

### 1. Deploy Backend

- Create two Lambda functions:
  - `TripLogWriter` → handles `POST /trips`
  - `TripLogFilter` → handles `GET /trips`
- Wire both to API Gateway routes:
  - `POST /trips` → TripLogWriter
  - `GET /trips` → TripLogFilter
- Enable CORS for both routes

### 2. DynamoDB Table

- Table name: `TripLog`
- Primary key: `tripId` (UUID)
- Attributes: `tripName`, `location`, `date`, `notes`, `sentiment`, `entities`

### 3. AWS Comprehend Integration

In `TripLogWriter`, call:

```python
comprehend.detect_sentiment(Text=notes, LanguageCode='en')
comprehend.detect_entities(Text=notes, LanguageCode='en')
```

Store `sentiment` and `entities` in DynamoDB.

### 4. Frontend Hosting

- Upload `index.html` to an S3 bucket
- Enable static website hosting
- Set permissions for public read access

---

## 🧪 Testing

- Submit a trip via the form
- Check DynamoDB for saved item
- Use sentiment filter dropdown to fetch matching trips

---

## 📦 Deployment Notes

- API Gateway uses automatic deployment to `prod`
- All routes are under:  
  `https://<api-id>.execute-api.<region>.amazonaws.com/prod/trips`

---

## 🙌 Credits

Built by Tammy with guidance from Microsoft Copilot.  
Powered by AWS Lambda, Comprehend, and DynamoDB.

---

## 🗺️ Next Steps

- 🗂️ Filter by entity (e.g., location or person)
- 📊 Sentiment dashboard
- 🗺️ Map integration with Leaflet or Mapbox
