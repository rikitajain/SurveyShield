console.log("Loaded from STATIC folder");

const SurveyShield = {

    async start(config) {

        let latitude = null;
        let longitude = null;

        if (navigator.geolocation) {

            try {

                const position = await new Promise((resolve, reject) => {

                    navigator.geolocation.getCurrentPosition(
                        resolve,
                        reject,
                        {
                            timeout: 5000
                        }
                    );

                });

                latitude = position.coords.latitude;
                longitude = position.coords.longitude;

            } catch (e) {

                console.log("Location permission denied.");

            }

        }

        const payload = {

            project_id: config.projectId,
            uuid: config.uuid,
            vendor: config.vendor,

            ip: "",

            country: config.country,

            browser: navigator.userAgent,

            device_id: this.generateDeviceId(),

            latitude: latitude,
            longitude: longitude

        };

        console.log("SurveyShield Payload", payload);

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/api/respondent/check",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(payload)
                }
            );

            const result = await response.json();

            console.log("SurveyShield Response", result);

            return result;

        } catch (error) {

            console.error("SurveyShield Error", error);

        }

    },

    generateDeviceId() {

        const raw = [
            navigator.userAgent,
            navigator.platform,
            navigator.language,
            screen.width,
            screen.height,
            screen.colorDepth,
            Intl.DateTimeFormat().resolvedOptions().timeZone
        ].join("|");

        return btoa(raw);

    }

};