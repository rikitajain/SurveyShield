const SurveyShield = {

    async start(config) {

        const payload = {

            project_id: config.projectId,
            uuid: config.uuid,
            vendor: config.vendor,

            ip: "",

            country: config.country,

            browser: navigator.userAgent,

            device_id: this.generateDeviceId(),

            latitude: null,
            longitude: null
        };

        console.log("SurveyShield Payload", payload);

        return payload;
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