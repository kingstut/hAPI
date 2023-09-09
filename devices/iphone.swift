import CoreHaptics
var hapticCapability: CHHapticDeviceCapability?

if CHHapticEngine.capabilitiesForHardware().supportsHaptics {
    hapticCapability = CHHapticEngine.capabilitiesForHardware()
} else {
    print("Device doesn't support Core Haptics")
    return
}

func playHaptic(patterns: [HapticPattern]) {
    guard CHHapticEngine.capabilitiesForHardware().supportsHaptics else {
        print("Device doesn't support Core Haptics")
        return
    }
    
    var events = [CHHapticEvent]()
    
    var relativeTime: TimeInterval = 0
    for pattern in patterns {
        let event = CHHapticEvent(
            eventType: .hapticTransient,
            parameters: [
                CHHapticEventParameter(parameterID: .hapticIntensity, value: pattern.intensity),
                CHHapticEventParameter(parameterID: .hapticSharpness, value: pattern.intensity)
            ],
            relativeTime: relativeTime
        )
        
        events.append(event)
        relativeTime += pattern.duration
    }
    
    do {
        let pattern = try CHHapticPattern(events: events, parameters: [])
        
        let engine = try CHHapticEngine()
        let player = try engine.makePlayer(with: pattern)
        
        try engine.start()
        try player.start(atTime: CHHapticTimeImmediate)
        
    } catch {
        print("Haptic playback error: \(error.localizedDescription)")
    }
}