console.log("Loaded from STATIC folder");

const SurveyShield = {

    async start(config) {

        let latitude = null;
        let longitude = null;
		
		let location_permission = "Unavailable";
		let location_accuracy = null;

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

				location_permission = "Granted";
		
				latitude = position.coords.latitude;
				longitude = position.coords.longitude;
				location_accuracy = position.coords.accuracy;

            } catch (e) {

				if (e.code === 1) {
		
					location_permission = "Denied";
		
				} else if (e.code === 2) {
		
					location_permission = "Unavailable";
		
				} else if (e.code === 3) {
		
					location_permission = "Timeout";
		
				} else {
		
					location_permission = "Unknown";
		
				}
		
				console.log("Location Error:", location_permission);

            }

        } else {

			location_permission = "Unavailable";

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
            longitude: longitude,
			
			location_permission,
			location_accuracy,

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