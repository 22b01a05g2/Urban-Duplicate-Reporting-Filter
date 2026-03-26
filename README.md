# Urban Duplicate Reporting Filter

## Project Overview

Urban issue reporting platforms often face the problem of duplicate submissions for the same issue. This leads to redundant data, inefficient handling, and difficulty in prioritizing actual problems.

The Urban Duplicate Reporting Filter addresses this challenge by detecting duplicate or similar reports using a combination of geographic proximity, image similarity, and issue type comparison.

---

## Motivation

This project was developed to solve a real-world problem observed in urban monitoring systems.

Multiple users frequently report the same issue such as potholes, garbage accumulation, or infrastructure damage. In the absence of a validation mechanism, these duplicate reports increase workload and reduce efficiency.

The objective of this project is to introduce a smart validation layer that filters duplicate reports before submission and improves the overall quality of collected data.

---

## System Workflow

### 1. Issue Submission
The user provides:
- An image of the issue  
- Location coordinates (latitude and longitude)  
- Issue type  

### 2. Processing
- Image features are extracted using a pre-trained MobileNet model  
- The new report is compared with existing reports using:
  - Location proximity check  
  - Cosine similarity for image comparison  

### 3. Matching Classification

| Match Level | Description |
|------------|------------|
| High Match | Same image and nearby location |
| Medium Match | Different image but nearby location |
| Low Match | Same location but different issue type |
| No Match | No similar reports found |

### 4. Decision Handling
- If matches exist, they are displayed in priority order and a confirmation popup is shown  
- If no match exists, the issue is submitted directly  

---

## Unique Features

- AI-based image similarity detection  
- Location-based filtering for nearby issue identification  
- Priority-based result ordering (High → Medium → Low)  
- Real-time duplicate detection before submission  
- User confirmation mechanism for potential duplicates  

---

## Test Cases and Sample Runs

### Test Case 1: New Issue (No Nearby Reports)

- Input: New image and new location  
- Output: No matches found and issue is submitted  

<p align="center">
  <img width="1920" height="1080" alt="Screenshot (93)" src="https://github.com/user-attachments/assets/740740b2-9185-45f1-81b4-b692bce73e80" />
  <img width="1920" height="1080" alt="Screenshot (94)" src="https://github.com/user-attachments/assets/9eab27a3-3aed-46d4-8d71-f0571cad6ad6" />
</p>



---

### Test Case 2: Nearby Location, Different Issue Type

- Scenario: First report is a pothole, second report is garbage at the same location  
- Output: Classified as Low Match and confirmation popup is shown  

<p align="center">
  <img width="1920" height="1080" alt="Screenshot (95)" src="https://github.com/user-attachments/assets/ac3d09f3-7f69-47ec-9aba-5375af1572a4" />
  <img width="1920" height="1080" alt="Screenshot (96)" src="https://github.com/user-attachments/assets/581141a1-d73d-40cb-bdbc-be8c88f30422" />
</p>

---

### Test Case 3: Nearby Location, Different Image, Same Issue Type

- Input: Different image but location is nearby  
- Output: Classified as Medium Match  

<p align="center">
  <img width="1920" height="1080" alt="Screenshot (99)" src="https://github.com/user-attachments/assets/7fc739fb-0838-45b4-9fbd-ed88e6d3dc71" />
</p>

---

### Test Case 4: Same Image and Nearby Location

- Input: Same image and nearby location  
- Output: High Match with highest priority (image similarity close to 1)  

<p align="center">
  <img width="1920" height="1080" alt="Screenshot (100)" src="https://github.com/user-attachments/assets/d4223259-567b-4248-a295-cd8b12a29ef1" />
</p>

---

### Test Case 5: Completely Different Location

- Input: Different location with a different issue (e.g., water leakage)  
- Output: No match found and issue is submitted directly  

<p align="center">
  <img width="1920" height="1080" alt="Screenshot (103)" src="https://github.com/user-attachments/assets/1b910d7b-e81d-4352-8fab-b620243b37dc" />
</p>

---

## Result Prioritization

Matched results are displayed in the following order:

High Match → Medium Match → Low Match  

This ensures that the most relevant duplicate reports are highlighted first for user awareness.

---

## Tech Stack

- Backend: Flask (Python)  
- Frontend: HTML, CSS, JavaScript  
- Deep Learning Model: MobileNet (feature extraction)  
- Similarity Measure: Cosine Similarity  
- Storage: Local file system for images and metadata  

---

## Future Enhancements

- Integration with databases such as PostgreSQL or MongoDB  
- Map-based visualization for reported issues  
- Improved deep learning models for higher accuracy  
- Scalable deployment as a web or mobile application  

---

## Author

Varshitha Samatham  
B.Tech Computer Science Engineering  

---
