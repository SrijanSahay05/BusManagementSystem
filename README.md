# BusManagementSystem
# BusManagementSystem

## Task Description: Bus Booking System

Develop a **Bus Booking System** using **Django** that enables passengers to book bus tickets and provides an admin interface to manage bus schedules. The system should be deployed using **Docker**, **Nginx**, and hosted on **DigitalOcean**. The development process is divided into phases to guide implementation.

---

## Phase 1: Basic Functionality

1. **Authentication**
    - Implement two types of login using [Django’s built-in authentication system](https://docs.djangoproject.com/en/stable/topics/auth/):
        - **Passengers**: Access the ticket booking section.
        - **Administrators**: Manage buses and schedules.
2. **Database Design**
    - Define a structured database using Django's [ORM](https://docs.djangoproject.com/en/stable/topics/db/models/):
        - Passengers can book tickets for multiple users (e.g., friends or family).
        - Ensure seat availability is checked before confirming bookings.
        - Admins can add new buses, specifying route details, timings, and seat availability.
        - Routes in this phase are direct, going from Bus Stop **A to Bus Stop B** without intermediate stops.
        - Implement a **wallet system** for users to add funds and use them for bookings (no payment gateway integration required).
3. **Administrative Functions**
    - Administrators can:
        1. View all current bookings for a specific bus.
        2. Add a new bus with its running schedule (days of the week the bus operates).
        3. Cancel an existing bus, refunding booked tickets by returning funds to passengers' wallets.
        4. Update bus fares and schedules.
4. **User Features**
    - Passengers can:
        - View past and upcoming journeys.
        - Cancel upcoming trips up to **6 hours** before departure.
        - Search for buses (e.g., from **City A** to **City B**) on the homepage.
        - Book tickets only if they have sufficient wallet balance.
        - Edit passenger details for booked tickets using a [ManyToMany relationship](https://docs.djangoproject.com/en/stable/topics/db/examples/many_to_many/).
        - Sort search results by departure time.

---

## Phase 2: Enhanced Functionality

1. **Google OAuth2 Login**
    - Integrate Google Login using [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/).
    - Allow users to view past trips and expenses after logging in with Google.
2. **Email Notifications and OTP Verification**
    - Send email notifications to passengers upon successful booking.
    - Implement OTP verification for actions like account registration or booking confirmation. Refer to [Implementing Email and Mobile OTP Verification in Django](https://dev.to/rupesh_mishra/implementing-email-and-mobile-otp-verification-in-django-a-comprehensive-guide-4oo0) for guidance.
    - Also send a verification email to the user when they sign up.
    - Make sure the OTP and the verification link have an expiry.
3. **Database Upgrade**
    - Transition from SQLite to **PostgreSQL** for production. [Refer to Django's database documentation](https://docs.djangoproject.com/en/stable/ref/databases/).
4. **Seat Classes**
    - Add different seat classes for buses (e.g., **General**, **Sleeper**, **Luxury**).
5. **Intermediate Stops and Routes**
    - Implement bus routes with multiple stops (e.g., **City A → City B → City C → City D**).
    - Allow passengers to book tickets for segments of the route (e.g., **City A to City C**).
6. **Administrative Export**
    - Provide an **Excel export feature** for administrators to download reservation details for a specific bus.

---

## Phase 3: Deployment

1. **Prepare for Production**
    - Containerize the Django project using **Docker**, ensuring separate containers for the application, database (PostgreSQL), and Nginx.
    - How to `Dockerize`
        - Docker in essential while developing applications to ensure a consistent development environment while collaborating. It makes many things easier while making large scale applications.
        - Containerize the entire Django application using Docker
        - Create a `Dockerfile` for the Django application
        - Develop a `docker-compose.yml` file to orchestrate multiple services:
            - Django web application (run using gunicorn)
            - PostgreSQL database
            - Nginx reverse proxy
        - Configure Nginx as a reverse proxy to handle incoming requests and serve static files
        - Implement volume mounts for persistent data storage (e.g., database data, static files)
        - You can follow these [article](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/) for dockerization.
        - Set up environment variables for sensitive information using [python-dotenv](https://pypi.org/project/python-dotenv/) (e.g., database credentials, secret keys,email passwords , etc…)
        - Optimize Docker images for production use (e.g., multi-stage builds, minimal base images)
2. **DigitalOcean Setup**
    - Sign up on DigitalOcean and create a droplet (virtual private server). Access the server via SSH.
3. **Domain and SSL**
    - Obtain a domain through providers like Namecheap or Microsoft Azure.
    - Secure the site with HTTPS using **Let's Encrypt**.
4. **Application Deployment**
    - Deploy the application using **Nginx**, **Gunicorn**, and **Docker**. Follow the tutorial [Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/) for guidance.
5. **Go Live**
    - Thoroughly test the application and access it through the assigned domain.

---

## Additional Features (Optional)

***Seat Selection and Waitlisting***

- Enable passengers to select specific seats during booking.
- If a bus is fully booked, allow users to join a waitlist and notify them through email if a seat becomes available.

---

## UX Suggestions

- Ensure proper role-based access:
    - Passengers should not have access to administrative functionalities.
    - Implement appropriate redirects for unauthorized access attempts.
- Add confirmation prompts for irreversible actions (e.g., canceling bookings or deleting buses).

---

## Submission Guidelines

### Submission Deadline: **16th February**

1. **GitHub Repository**
    - Upload the project to GitHub.
    - **Regularly update your code** on GitHub throughout the development process.
    - Ensure the repository is well-structured and includes the following:
        - A clear `README.md` file with setup and deployment instructions.
        - A `requirements.txt` file listing all the dependencies used in the project.
        - Any additional documentation to help understand and test the system.

1. **Security**
    - Do not expose sensitive data like the Django secret key, database credentials, or API keys.
    - Use environment variables for sensitive data and exclude them from version control.
2. **Documentation**
    - Include clear instructions on setting up and deploying the application.
3. **Testing**
    - Ensure the application is fully functional and free of bugs before submission.

Your code repository should be **frequently updated** during the development process.

**Tip**: Commit regularly to showcase progress (e.g., after implementing features or resolving bugs). The frequency and quality of updates will be **considered during evaluation.**

## Submission

Deadline: 16 Feb

Make sure to keep updating your code on github

---

By following these phases and guidelines, you will develop a robust, scalable, and user-friendly **Bus Booking System**.