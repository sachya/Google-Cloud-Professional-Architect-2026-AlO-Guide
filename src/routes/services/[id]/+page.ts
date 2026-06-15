import { error } from '@sveltejs/kit';
import services from '$lib/data/services.json';

export async function load({ params }: any) {
    const serviceSummary = services.find((s: any) => s.id === params.id);
    
    if (!serviceSummary) {
        throw error(404, 'Service not found');
    }
    
    try {
        // Dynamically import the service details JSON file
        const details = await import(`../../../lib/data/details/${params.id}.json`);
        return {
            service: {
                ...serviceSummary,
                ...details.default
            }
        };
    } catch (e) {
        // Fallback if details file is not generated yet
        return {
            service: {
                ...serviceSummary,
                keyPoints: [],
                scenarios: [],
                commands: []
            }
        };
    }
}

