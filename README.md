LongestCocoa
============

Programmers who write Objective-C must **REALLY** love its descriptive and verbose naming style. 

SoWhatAreTheLongestMethodOrConstantNamesInCocoaFramework? Here are some superb ones:

* outputImageProviderFromBufferWithPixelFormat:pixelsWide:pixelsHigh:baseAddress:bytesPerRow:releaseCallback:releaseContext:colorSpace:shouldColorMatch:
* kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange

Run `python longest.py` to discover the first 10 longest names for each identifier type. Below is the output from `python longest.py iphoneos` and `python longest.py macosx`.


Longest Names For iPhoneOS armv7
================

Longest Objective-C Interface Names
----------------
* [47] AVAssetResourceLoadingContentInformationRequest
* [45] UICollectionViewFlowLayoutInvalidationContext
* [41] AVMutableVideoCompositionLayerInstruction
* [41] UICollectionViewLayoutInvalidationContext
* [37] AVAsynchronousVideoCompositionRequest
* [36] AVMutableVideoCompositionInstruction
* [36] UIPercentDrivenInteractiveTransition
* [36] AVAssetWriterInputPixelBufferAdaptor
* [36] GKFriendRequestComposeViewController
* [35] AVVideoCompositionCoreAnimationTool

Longest Objective-C Protocol Names
----------------
* [44] UIViewControllerTransitionCoordinatorContext
* [44] GKFriendRequestComposeViewControllerDelegate
* [44] AVCaptureAudioDataOutputSampleBufferDelegate
* [44] AVCaptureVideoDataOutputSampleBufferDelegate
* [43] GKTurnBasedMatchmakerViewControllerDelegate
* [42] ABPeoplePickerNavigationControllerDelegate
* [40] UIViewControllerInteractiveTransitioning
* [39] UIDocumentInteractionControllerDelegate
* [38] AVCaptureMetadataOutputObjectsDelegate
* [38] MFMessageComposeViewControllerDelegate

Longest Objective-C Property Names
----------------
* [56] automaticallyEnablesStillImageStabilizationWhenAvailable
* [54] availableMediaCharacteristicsWithMediaSelectionOptions
* [49] outputObscuredDueToInsufficientExternalProtection
* [47] usesExternalPlaybackWhileExternalScreenIsActive
* [46] automaticallyEnablesLowLightBoostWhenAvailable
* [46] automaticallyConfiguresApplicationAudioSession
* [45] requiredPixelBufferAttributesForRenderContext
* [44] modalPresentationCapturesStatusBarAppearance
* [42] usesAirPlayVideoWhileAirPlayScreenIsActive
* [42] providesPresentationContextTransitionStyle

Longest Objective-C Method Names
----------------
* [128] initRecurrenceWithFrequency:interval:daysOfTheWeek:daysOfTheMonth:monthsOfTheYear:weeksOfTheYear:daysOfTheYear:setPositions:end:
* [120] drawStrikethroughForGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:
* [115] layoutManager:boundingBoxForControlGlyphAtIndex:forTextContainer:proposedLineFragment:glyphPosition:characterIndex:
* [113] decimalNumberHandlerWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:
* [112] drawUnderlineForGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:
* [111] getLineFragmentInsertionPointsForCharacterAtIndex:alternatePositions:inDisplayOrder:positions:characterIndexes:
* [108] migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:
* [104] videoComposition:shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction:layerInstruction:asset:
* [101] animateWithDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:
* [98] strikethroughGlyphRange:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:

Longest Objective-C Method Names (0/1 Parameter)
----------------
* [70] automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers
* [65] navigationControllerPreferredInterfaceOrientationForPresentation:
* [64] splitViewControllerPreferredInterfaceOrientationForPresentation:
* [63] pageViewControllerPreferredInterfaceOrientationForPresentation:
* [61] tabBarControllerPreferredInterfaceOrientationForPresentation:
* [60] backButtonBackgroundVerticalPositionAdjustmentForBarMetrics:
* [60] setAutomaticallyEnablesStillImageStabilizationWhenAvailable:
* [59] generateIdentityVerificationSignatureWithCompletionHandler:
* [57] recommendedVideoSettingsForAssetWriterWithOutputFileType:
* [57] recommendedAudioSettingsForAssetWriterWithOutputFileType:

Longest C Function Names
----------------
* [63] CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback
* [62] CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType
* [62] CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers
* [62] MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics
* [61] CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes
* [58] CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes
* [58] CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS
* [57] ABAddressBookCopyArrayOfAllPeopleInSourceWithSortOrdering
* [57] vImageMultiDimensionalInterpolatedLookupTable_Planar16Q12
* [57] vImageAlphaBlend_NonpremultipliedToPremultiplied_ARGB8888

Longest Enum Names
----------------
* [41] NSPersistentStoreUbiquitousTransitionType
* [41] UIPageViewControllerNavigationOrientation
* [40] UIImagePickerControllerCameraCaptureMode
* [39] UIPageViewControllerNavigationDirection
* [38] UIImagePickerControllerCameraFlashMode
* [38] CBPeripheralManagerAuthorizationStatus
* [36] NSAttributedStringEnumerationOptions
* [36] NSURLSessionAuthChallengeDisposition
* [36] CBPeripheralManagerConnectionLatency
* [35] UIImagePickerControllerCameraDevice

Longest Enum Constant Names
----------------
* [64] kCFStreamErrorHTTPSProxyFailureUnexpectedResponseToCONNECTMethod
* [63] NSPersistentStoreUbiquitousTransitionTypeInitialImportCompleted
* [63] NSDataWritingFileProtectionCompleteUntilFirstUserAuthentication
* [61] kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualTo
* [61] NSAttributedStringEnumerationLongestEffectiveRangeNotRequired
* [58] kCMBufferQueueTrigger_WhenDurationBecomesLessThanOrEqualTo
* [58] kAudioSessionProperty_OverrideCategoryEnableBluetoothInput
* [57] kCMBufferQueueTrigger_WhenMaxPresentationTimeStampChanges
* [57] kAudioFileGlobalInfo_AvailableStreamDescriptionsForFormat
* [57] AVAudioSessionRouteChangeReasonNoSuitableRouteForCategory

Longest Variable Constant Names
----------------
* [96] kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange
* [81] kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection
* [74] MFMessageComposeViewControllerTextMessageAvailabilityDidChangeNotification
* [71] kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection
* [66] kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight
* [64] kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS
* [64] kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged
* [64] AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly
* [64] kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS
* [62] NSPersistentStoreDidImportUbiquitousContentChangesNotification


Longest Names For MacOSX x86_64
================

Longest Objective-C Interface Names
----------------
* [43] ICScannerFunctionalUnitPositiveTransparency
* [43] ICScannerFunctionalUnitNegativeTransparency
* [41] AVMutableVideoCompositionLayerInstruction
* [37] ICScannerFunctionalUnitDocumentFeeder
* [36] GKFriendRequestComposeViewController
* [36] AVMutableVideoCompositionInstruction
* [36] AVAssetWriterInputPixelBufferAdaptor
* [35] IOBluetoothDeviceSelectorController
* [35] AVAssetReaderVideoCompositionOutput
* [35] GKTurnBasedMatchmakerViewController

Longest Objective-C Protocol Names
----------------
* [49] IMServiceApplicationGroupListAuthorizationSupport
* [44] GKFriendRequestComposeViewControllerDelegate
* [44] AVCaptureAudioDataOutputSampleBufferDelegate
* [44] IMServicePlugInGroupListAuthorizationSupport
* [44] AVCaptureVideoDataOutputSampleBufferDelegate
* [44] IMServicePlugInGroupListHandlePictureSupport
* [43] IMServiceApplicationInstantMessagingSupport
* [43] GKTurnBasedMatchmakerViewControllerDelegate
* [40] IOBluetoothHandsFreeAudioGatewayDelegate
* [39] IMServicePlugInGroupListOrderingSupport

Longest Objective-C Property Names
----------------
* [54] availableMediaCharacteristicsWithMediaSelectionOptions
* [41] animatesToStartingPositionsOnCancelOrFail
* [40] incrementalSearchingShouldDimContentView
* [40] acceptsThresholdForBlackAndWhiteScanning
* [40] defaultThresholdForBlackAndWhiteScanning
* [37] usesThresholdForBlackAndWhiteScanning
* [37] displaysPostProcessApplicationControl
* [36] availableImageDataCVPixelFormatTypes
* [34] requireAdministratorForAssociation
* [34] automaticallyAdjustsVideoMirroring

Longest Objective-C Method Names
----------------
* [150] outputImageProviderFromBufferWithPixelFormat:pixelsWide:pixelsHigh:baseAddress:bytesPerRow:releaseCallback:releaseContext:colorSpace:shouldColorMatch:
* [148] initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bitmapFormat:bytesPerRow:bitsPerPixel:
* [140] outputImageProviderFromTextureWithPixelFormat:pixelsWide:pixelsHigh:name:flipped:releaseCallback:releaseContext:colorSpace:shouldColorMatch:
* [137] getLineFragmentRect:usedRect:remainingRect:forStartingGlyphAtIndex:proposedRect:lineSpacing:paragraphSpacingBefore:paragraphSpacingAfter:
* [135] initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:
* [133] initMouseEvent:canBubble:cancelable:view:detail:screenX:screenY:clientX:clientY:ctrlKey:altKey:shiftKey:metaKey:button:relatedTarget:
* [128] keyEventWithType:location:modifierFlags:timestamp:windowNumber:context:characters:charactersIgnoringModifiers:isARepeat:keyCode:
* [128] initRecurrenceWithFrequency:interval:daysOfTheWeek:daysOfTheMonth:monthsOfTheYear:weeksOfTheYear:daysOfTheYear:setPositions:end:
* [120] geometrySourceWithData:semantic:vectorCount:floatComponents:componentsPerVector:bytesPerComponent:dataOffset:dataStride:
* [120] drawStrikethroughForGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:

Longest Objective-C Method Names (0/1 Parameter)
----------------
* [68] managedObjectContextsToMonitorWhenSyncingPersistentStoreCoordinator:
* [68] managedObjectContextsToReloadAfterSyncingPersistentStoreCoordinator:
* [56] requestNotificationOfMediaDataChangeWithAdvanceInterval:
* [55] captureOutputShouldProvideSampleAccurateRecordingStart:
* [54] availableMediaCharacteristicsWithMediaSelectionOptions
* [54] loadDefaultLeaderboardCategoryIDWithCompletionHandler:
* [54] accommodatePresentedItemDeletionWithCompletionHandler:
* [52] continueWithoutCredentialForAuthenticationChallenge:
* [52] chapterMetadataGroupsBestMatchingPreferredLanguages:
* [52] associatedMediaSelectionOptionInMediaSelectionGroup:

Longest C Function Names
----------------
* [68] IOBluetoothOBEXSessionCreateWithIOBluetoothDeviceRefAndChannelNumber
* [64] IOBluetoothOBEXSessionCreateWithIncomingIOBluetoothRFCOMMChannel
* [63] CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback
* [63] IOBluetoothServiceBrowserControllerDiscoverWithDeviceAttributes
* [62] CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType
* [62] CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers
* [62] IOBluetoothOBEXSessionCreateWithIOBluetoothSDPServiceRecordRef
* [61] CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes
* [60] IOBluetoothRegisterForFilteredRFCOMMChannelOpenNotifications
* [59] IOBluetoothRegisterForFilteredL2CAPChannelOpenNotifications

Longest Enum Names
----------------
* [47] BluetoothLESecurityManagerKeyDistributionFormat
* [44] BluetoothHCIExtendedInquiryResponseDataTypes
* [43] IOBluetoothUserNotificationChannelDirection
* [41] BluetoothAuthenticationRequirementsValues
* [39] BluetoothHCITransmitReadPowerLevelTypes
* [38] SDPAttributeDeviceIdentificationRecord
* [37] BluetoothHCIRetransmissionEffortTypes
* [37] BluetoothHCIAFHChannelAssessmentModes
* [36] BluetoothHCIGeneralFlowControlStates
* [36] BluetoothHCIDeleteStoredLinkKeyFlags

Longest Enum Constant Names
----------------
* [88] kBluetoothAMPManagerCreatePhysicalLinkResponseAMPDisconnectedPhysicalLinkRequestReceived
* [84] kBluetoothHCIExtendedInquiryResponseDataType128BitServiceClassUUIDsWithMoreAvailable
* [83] kBluetoothHCIExtendedInquiryResponseDataType32BitServiceClassUUIDsWithMoreAvailable
* [83] kBluetoothHCIExtendedInquiryResponseDataType16BitServiceClassUUIDsWithMoreAvailable
* [79] kBluetoothHCIExtendedInquiryResponseDataType128BitServiceClassUUIDsCompleteList
* [78] kBluetoothHCIExtendedInquiryResponseDataType32BitServiceClassUUIDsCompleteList
* [78] kBluetoothHCIExtendedInquiryResponseDataType16BitServiceClassUUIDsCompleteList
* [77] kBluetoothAuthenticationRequirementsMITMProtectionNotRequiredDedicatedBonding
* [75] kBluetoothAuthenticationRequirementsMITMProtectionNotRequiredGeneralBonding
* [74] kBluetoothHCIExtendedInquiryResponseDataTypeServiceSolicitation128BitUUIDs

Longest Variable Constant Names
----------------
* [96] kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange
* [78] kVTDecompressionPropertyKey_MaxOutputPresentationTimeStampOfFramesBeingDecoded
* [78] kVTDecompressionPropertyKey_MinOutputPresentationTimeStampOfFramesBeingDecoded
* [69] kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByPerformance
* [68] kVTDecompressionPropertyKey_PixelFormatsWithReducedResolutionSupport
* [65] kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByQuality
* [64] kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS
* [64] kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS
* [64] kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged
* [62] NSPersistentStoreDidImportUbiquitousContentChangesNotification